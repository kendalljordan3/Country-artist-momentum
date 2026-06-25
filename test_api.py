from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("YOUTUBE_API_KEY")
print("API key loaded: " + str(api_key[:5]) + "...")