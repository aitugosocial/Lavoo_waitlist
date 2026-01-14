import uvicorn
import os
from dotenv import load_dotenv
from api import app

# Load environment variables
load_dotenv()

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(
        "api:app",
        host="0.0.0.0",
        port=port,
        reload=False  # Disable reload to prevent ghost processes
    )
