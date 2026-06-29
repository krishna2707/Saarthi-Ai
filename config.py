from dotenv import load_dotenv
import os

load_dotenv()

SPOTIFY_CLIENT_ID=os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET=os.getenv("SPOTIFY_CLIENT_SECRET")
GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")
SARVAM_API_KEY=os.getenv("SARVAM_API_KEY")