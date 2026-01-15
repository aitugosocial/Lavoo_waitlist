from fastapi import FastAPI, Depends, HTTPException, Form
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from db import get_db, engine
from db.models import Base, Waitlist
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create FastAPI app
app = FastAPI(title="Lavoo Waitlist API", version="1.0.0")

# Configure CORS to allow frontend to communicate with backend
origins = [
    "http://localhost:3000",
    "http://localhost:3001",
    "http://localhost:5173",
    "http://localhost:8080"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from fastapi import Request

@app.middleware("http")
async def log_requests(request: Request, call_next):
    # Reduced logging noise for production
    if request.url.path != "/":  # Skip health check spam
        logger.info(f"INCOMING REQUEST: {request.method} {request.url.path}")
    response = await call_next(request)
    return response

# Create database tables
# logger.info("Connecting to DB engine for initialization...")
Base.metadata.create_all(bind=engine)
# logger.info("Database tables initialized.")

@app.get("/")
def read_root():
    """Root endpoint to verify API is running"""
    return {
        "message": "LAVOO WAITLIST API ACTIVE", 
        "status": "healthy"
    }

@app.post("/api/waitlist")
async def add_to_waitlist(
    email: str = Form(...),
    db: Session = Depends(get_db)
):
    """
    Add an email to the waitlist.
    
    Args:
        email: User's email address (from form data)
        db: Database session
        
    Returns:
        Success message with email confirmation
        
    Raises:
        HTTPException: If email already exists or validation fails
    """
    try:
        # Normalize email
        normalized_email = email.lower().strip()
        logger.info(f"Processing waitlist request for: {normalized_email}")
        
        # Validate email format (basic check)
        if not normalized_email or "@" not in normalized_email or "." not in normalized_email:
            logger.warning(f"Validation failed for: {normalized_email}")
            raise HTTPException(
                status_code=400,
                detail="Invalid email format"
            )
        
        # Check if email already exists in the waitlist
        existing_entry = db.query(Waitlist).filter(Waitlist.email == normalized_email).first()
        
        if existing_entry:
            logger.info(f"Email already waitlisted: {normalized_email}")
            raise HTTPException(
                status_code=409,
                detail="This email has already been waitlisted"
            )
        
        # Create new waitlist entry
        new_entry = Waitlist(email=normalized_email)
        
        # Add to database
        db.add(new_entry)
        db.commit()
        db.refresh(new_entry)
        
        logger.info(f"Successfully added {normalized_email} to waitlist (ID: {new_entry.id})")
        
        return {
            "success": True,
            "message": "You have been successfully waitlisted!",
            "email": new_entry.email,
            "id": new_entry.id
        }
        
    except HTTPException:
        # Re-raise HTTP exceptions (including our duplicate check)
        raise
        
    except Exception as e:
        db.rollback()
        logger.error(f"Error adding to waitlist: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail="An error occurred while processing your request"
        )

@app.get("/api/waitlist/count")
async def get_waitlist_count(db: Session = Depends(get_db)):
    """
    Get the total number of people on the waitlist.
    
    Returns:
        Total count of waitlist entries
    """
    try:
        count = db.query(Waitlist).count()
        return {"count": count}
    except Exception as e:
        logger.error(f"Error getting waitlist count: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail="An error occurred while fetching waitlist count"
        )

# Serve static files (Frontend) - MUST BE LAST
import os
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

# Check if the build output directory exists (production mode)
if os.path.exists("out"):
    # Mount the assets folder separately to avoid conflict with root catch-all
    # Vite places assets in out/assets
    if os.path.exists("out/assets"):
        app.mount("/assets", StaticFiles(directory="out/assets"), name="assets")

    # Serve the main index.html for the root path and any other path (SPA support)
    @app.get("/{full_path:path}")
    async def serve_spa(full_path: str):
        # Allow API routes to pass through (though they should be matched above)
        if full_path.startswith("api"):
            raise HTTPException(status_code=404, detail="API route not found")
        
        # Check if the file exists in the out directory (e.g., favicon.ico, etc.)
        file_path = os.path.join("out", full_path)
        if os.path.exists(file_path) and os.path.isfile(file_path):
             return FileResponse(file_path)
        
        # Fallback to index.html for SPA routing
        return FileResponse("out/index.html")

