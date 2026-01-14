
import requests
import sys
import time

def check_backend():
    print("1. Checking Direct Backend Connection (Port 8001)...")
    try:
        r = requests.get("http://localhost:8001/")
        print(f"   ✅ Backend is UP: {r.status_code} - {r.json()}")
        return True
    except Exception as e:
        print(f"   ❌ Backend is DOWN: {e}")
        return False

def check_proxy():
    print("\n2. Checking Vite Proxy Connection (Port 3000)...")
    try:
        # We try to hit the backend THROUGH the frontend proxy
        r = requests.post("http://localhost:3000/api/waitlist", data={"email": "test_script@test.com"})
        
        if r.status_code == 404:
            print("   ❌ Proxy Failed (404 Not Found). Vite is not forwarding '/api'.")
        elif r.status_code == 200 and "<!doctype html>" in r.text.lower():
             print("   ❌ Proxy Failed. Vite returned HTML (SPA Fallback) instead of API response.")
        elif r.status_code in [200, 409, 400, 422]:
            print(f"   ✅ Proxy is WORKING! Received API status: {r.status_code}")
            return True
        else:
            print(f"   ❓ Unknown Response: {r.status_code}")
            
    except Exception as e:
        print(f"   ❌ Could not connect to Frontend (Port 3000): {e}")
        return False

if __name__ == "__main__":
    print("="*50)
    print("   LAVOO CONNECTION DIAGNOSTIC")
    print("="*50)
    
    bk = check_backend()
    if bk:
        check_proxy()
    else:
        print("\n⚠️ Fix the backend first before testing the proxy.")
