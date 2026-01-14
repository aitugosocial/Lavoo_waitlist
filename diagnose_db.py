"""
Diagnostic script to check database connection and test insertion
"""
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from db.models import Base, Waitlist
import sys

# Load environment variables
load_dotenv()

print("=" * 70)
print("DATABASE CONNECTION DIAGNOSTIC")
print("=" * 70)

# Step 1: Check if DATABASE_URL is loaded
DATABASE_URL = os.getenv("DATABASE_URL")
print(f"\n1. DATABASE_URL loaded: {'YES' if DATABASE_URL else 'NO'}")

if DATABASE_URL:
    print(f"   Length: {len(DATABASE_URL)} characters")
    print(f"   First 50 chars: {DATABASE_URL[:50]}...")
    print(f"   Contains '&amp;': {'YES - THIS IS THE PROBLEM!' if '&amp;' in DATABASE_URL else 'NO'}")
    print(f"   Contains '&': {'YES' if '&' in DATABASE_URL else 'NO'}")
else:
    print("   ERROR: DATABASE_URL is None!")
    sys.exit(1)

# Step 2: Try to create engine
print(f"\n2. Creating database engine...")
try:
    engine = create_engine(DATABASE_URL, echo=True)
    print("   ✓ Engine created successfully")
except Exception as e:
    print(f"   ✗ Failed to create engine: {e}")
    sys.exit(1)

# Step 3: Test connection
print(f"\n3. Testing database connection...")
try:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        print("   ✓ Connection successful!")
except Exception as e:
    print(f"   ✗ Connection failed: {e}")
    print("\n   LIKELY CAUSE: The '&amp;' in your .env file should be '&'")
    sys.exit(1)

# Step 4: Create tables
print(f"\n4. Creating tables...")
try:
    Base.metadata.create_all(bind=engine)
    print("   ✓ Tables created/verified")
except Exception as e:
    print(f"   ✗ Failed to create tables: {e}")
    sys.exit(1)

# Step 5: Test insertion
print(f"\n5. Testing email insertion...")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = SessionLocal()

try:
    test_email = "diagnostic@test.com"
    
    # Check if exists
    existing = db.query(Waitlist).filter(Waitlist.email == test_email).first()
    if existing:
        print(f"   ℹ Test email already exists (ID: {existing.id})")
        print(f"   ✓ Database read works!")
    else:
        # Insert new
        new_entry = Waitlist(email=test_email)
        db.add(new_entry)
        db.commit()
        db.refresh(new_entry)
        print(f"   ✓ Email inserted successfully (ID: {new_entry.id})")
    
    # Get count
    count = db.query(Waitlist).count()
    print(f"   ✓ Total emails in waitlist: {count}")
    
except Exception as e:
    print(f"   ✗ Database operation failed: {e}")
    db.rollback()
    sys.exit(1)
finally:
    db.close()

print("\n" + "=" * 70)
print("DIAGNOSIS COMPLETE")
print("=" * 70)
print("✓ All checks passed! Database is working correctly.")
print("\nIf you're still having issues with the API:")
print("1. Make sure you restart the server after fixing .env")
print("2. Check the server logs for any errors")
print("3. Run: python test_api.py")
