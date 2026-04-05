import os
from datetime import datetime
import pytz
from dotenv import load_dotenv

from fastapi import FastAPI
from pydantic import BaseModel

from google.adk import Agent
from google.adk.tools.langchain_tool import LangchainTool

from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

# --- Load environment variables ---
load_dotenv()

MODEL = os.getenv("MODEL", "gemini-2.5-flash")

# --- Wikipedia Tool ---
wiki_tool = LangchainTool(
    tool=WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
)

# --- REAL-TIME TOOL (FIXED) ---
def get_current_datetime() -> str:
    """Returns current date and time in India"""
    india = pytz.timezone("Asia/Kolkata")
    return datetime.now(india).strftime("%Y-%m-%d %H:%M:%S IST")

# --- Root Agent ---
root_agent = Agent(
    name="smart_qa_agent",
    model=MODEL,
    description="AI agent for QA + coding + real-time info",
    instruction="""
You are a smart AI assistant.

CAPABILITIES:
- Answer general knowledge questions
- Generate programming code (Python, C, Java, etc.)
- Explain code clearly
- Help with debugging

SPECIAL RULE:
- If user asks about current date or time → use the datetime tool

RULES:
- For coding questions → provide clean, correct, well-formatted code
- Add short explanation when helpful
- Use Wikipedia only if needed
- Never mention tools

STYLE:
- Keep answers clear and concise
- Format code properly
- Be confident and helpful
""",
    tools=[wiki_tool, get_current_datetime],  # ADDED TOOL
)

# --- FastAPI app ---
app = FastAPI()

class QueryRequest(BaseModel):
    query: str

@app.post("/ask")
def ask(request: QueryRequest):
    response = root_agent.run(request.query)
    return {"response": response}

@app.get("/")
def health():
    return {"status": "running 🚀"}