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
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from fastapi import Request

@app.middleware("http")
async def log_requests(request: Request, call_next):
    print(f"\n🔍 INCOMING REQUEST: {request.method} {request.url.path}")
    response = await call_next(request)
    print(f"✅ REQUEST COMPLETED: {response.status_code}\n")
    return response

# Create database tables
print(f"DEBUG: Connecting to DB engine for initialization...")
Base.metadata.create_all(bind=engine)
print("DEBUG: Database tables initialized.")

@app.get("/")
def read_root():
    """Root endpoint to verify API is running"""
    return {
        "message": "LAVOO WAITLIST API ACTIVE ON PORT 8001", 
        "status": "healthy",
        "port": 8001
    }

@app.post("/api/waitlist")
async def add_to_waitlist(
    email: str = Form(...),
    db: Session = Depends(get_db)
):
    # CRITICAL DEBUG: Ensure we see requests in the terminal
    print("\n" + "="*50)
    print(f"🚀 CRITICAL: REQUEST RECEIVED for email: {email}")
    print("="*50 + "\n")
    
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
        print(f"DEBUG: Processing email: {normalized_email}")
        
        # Validate email format (basic check)
        if not normalized_email or "@" not in normalized_email or "." not in normalized_email:
            print(f"DEBUG: Validation failed for: {normalized_email}")
            raise HTTPException(
                status_code=400,
                detail="Invalid email format"
            )
        
        # Normalize email
        normalized_email = email.lower().strip()
        
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
