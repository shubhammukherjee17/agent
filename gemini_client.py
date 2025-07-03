import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Get the API key from the .env file
api_key = os.getenv("GEMINI_API_KEY")

# Check if the API key is loaded correctly
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

# Configure Gemini client
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create a Gemini model instance
model = genai.GenerativeModel("gemini-2.5-pro")  # Update name as needed

def generate_response(prompt: str) -> str:
    """Generate text using Gemini."""
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Error generating response: {e}")
        return "An error occurred while generating the response."
