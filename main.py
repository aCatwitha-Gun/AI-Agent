import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

def validate_environment():
    required_vars = ["GEMINI_API_KEY"]

    for var in required_vars:
        if var not in os.environ:
            # Raise a RuntimeError to stop execution
            raise RuntimeError(f"Missing required environment variable: {var}")