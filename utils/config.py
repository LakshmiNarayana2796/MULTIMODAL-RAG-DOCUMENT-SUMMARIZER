import os
#from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

INPUT_PATH = os.getcwd()
OUTPUT_PATH = os.path.join(os.getcwd(), "figures")
# Load environment variables
load_dotenv()

import pytesseract
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Environment variable setup
groq_api_key = os.getenv("GROQ_API_KEY")
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)