import os
from dotenv import load_dotenv

load_dotenv()

# Gemini API Key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Database URL (will be used later)
DATABASE_URL = os.getenv("DATABASE_URL")