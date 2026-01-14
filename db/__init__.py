from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get database URL from environment
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is not set! Check your .env file.")

# Log the database connection (hide password)
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
safe_url = DATABASE_URL.split('@')[1] if '@' in DATABASE_URL else 'unknown'
logger.info(f"Connecting to database: ...@{safe_url}")

# Create database engine with echo enabled for debugging
engine = create_engine(DATABASE_URL, echo=False, pool_pre_ping=True)

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get database session
def get_db():
    """
    Dependency function to get database session.
    Yields a database session and ensures it's closed after use.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
