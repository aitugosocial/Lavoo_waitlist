import os
from dotenv import load_dotenv
import requests

# Load environment variables
load_dotenv()

port = os.getenv("PORT", "8000")
BASE_URL = f"http://localhost:{port}"

def test_api_health():
    """Test if API is running"""
    print("Testing API health...")
    try:
        response = requests.get(f"{BASE_URL}/")
        if response.status_code == 200:
            print("✓ API is running!")
            print(f"  Response: {response.json()}")
            return True
        else:
            print(f"✗ API returned status {response.status_code}")
            return False
    except Exception as e:
        print(f"✗ Cannot connect to API: {e}")
        print("  Make sure the server is running with 'python main.py'")
        return False

def test_add_email(email):
    """Test adding an email to waitlist"""
    print(f"\nTesting email submission: {email}")
    try:
        response = requests.post(
            f"{BASE_URL}/api/waitlist",
            data={"email": email}
        )
        
        if response.status_code == 200:
            data = response.json()
            print(f"✓ Email added successfully!")
            print(f"  Message: {data.get('message')}")
            print(f"  Email: {data.get('email')}")
            print(f"  ID: {data.get('id')}")
            return True
        elif response.status_code == 409:
            error = response.json()
            print(f"✓ Duplicate detected (as expected)")
            print(f"  Message: {error.get('detail')}")
            return True
        else:
            error = response.json()
            print(f"✗ Error: {error.get('detail')}")
            return False
    except Exception as e:
        print(f"✗ Request failed: {e}")
        return False

def test_get_count():
    """Test getting waitlist count"""
    print("\nTesting waitlist count...")
    try:
        response = requests.get(f"{BASE_URL}/api/waitlist/count")
        if response.status_code == 200:
            data = response.json()
            print(f"✓ Current waitlist count: {data.get('count')}")
            return True
        else:
            print(f"✗ Failed to get count: {response.status_code}")
            return False
    except Exception as e:
        print(f"✗ Request failed: {e}")
        return False

if __name__ == "__main__":
    print("=" * 60)
    print("LAVOO WAITLIST API TEST")
    print("=" * 60)
    
    # Test 1: API Health
    health_ok = test_api_health()
    
    if not health_ok:
        print("\n✗ API is not running. Please start it with 'python main.py'")
        exit(1)
    
    # Test 2: Add new email
    import time
    test_email = f"test_{int(time.time())}@example.com"
    add_ok = test_add_email(test_email)
    
    # Test 3: Try adding same email (should detect duplicate)
    duplicate_ok = test_add_email(test_email)
    
    # Test 4: Get count
    count_ok = test_get_count()
    
    # Summary
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    print(f"API Health: {'PASS' if health_ok else 'FAIL'}")
    print(f"Email Addition: {'PASS' if add_ok else 'FAIL'}")
    print(f"Duplicate Detection: {'PASS' if duplicate_ok else 'FAIL'}")
    print(f"Count Query: {'PASS' if count_ok else 'FAIL'}")
    
    if all([health_ok, add_ok, duplicate_ok, count_ok]):
        print("\n✓ All tests passed! The waitlist API is working correctly.")
    else:
        print("\n✗ Some tests failed. Please check the errors above.")
