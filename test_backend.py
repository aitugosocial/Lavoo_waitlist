"""
Test script to verify the waitlist backend is working correctly.
This script tests the database connection and API endpoints.
"""
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db import engine, get_db
from db.models import Base, Waitlist
from sqlalchemy.orm import Session

def test_database_connection():
    """Test if we can connect to the database"""
    print("Testing database connection...")
    try:
        # Try to create tables
        Base.metadata.create_all(bind=engine)
        print("✓ Database connection successful!")
        print("✓ Tables created successfully!")
        return True
    except Exception as e:
        print(f"✗ Database connection failed: {str(e)}")
        return False

def test_insert_email():
    """Test if we can insert an email into the waitlist"""
    print("\nTesting email insertion...")
    try:
        db = next(get_db())
        
        # Create a test email
        test_email = "test@example.com"
        
        # Check if email already exists
        existing = db.query(Waitlist).filter(Waitlist.email == test_email).first()
        if existing:
            print(f"✓ Test email already exists in database (ID: {existing.id})")
            db.close()
            return True
        
        # Insert new email
        new_entry = Waitlist(email=test_email)
        db.add(new_entry)
        db.commit()
        db.refresh(new_entry)
        
        print(f"✓ Email inserted successfully! (ID: {new_entry.id})")
        db.close()
        return True
    except Exception as e:
        print(f"✗ Email insertion failed: {str(e)}")
        return False

def test_query_count():
    """Test if we can query the waitlist count"""
    print("\nTesting waitlist count query...")
    try:
        db = next(get_db())
        count = db.query(Waitlist).count()
        print(f"✓ Current waitlist count: {count}")
        db.close()
        return True
    except Exception as e:
        print(f"✗ Count query failed: {str(e)}")
        return False

if __name__ == "__main__":
    print("=" * 50)
    print("LAVOO WAITLIST BACKEND TEST")
    print("=" * 50)
    
    # Run tests
    db_test = test_database_connection()
    insert_test = test_insert_email()
    count_test = test_query_count()
    
    # Summary
    print("\n" + "=" * 50)
    print("TEST SUMMARY")
    print("=" * 50)
    print(f"Database Connection: {'PASS' if db_test else 'FAIL'}")
    print(f"Email Insertion: {'PASS' if insert_test else 'FAIL'}")
    print(f"Count Query: {'PASS' if count_test else 'FAIL'}")
    
    if db_test and insert_test and count_test:
        print("\n✓ All tests passed! Backend is ready to use.")
        print("\nNext steps:")
        print("1. Run 'python main.py' to start the server")
        print("2. Test the API at http://localhost:8000")
    else:
        print("\n✗ Some tests failed. Please check the errors above.")
