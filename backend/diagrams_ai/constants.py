from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()
LLM_CLIENT = OpenAI(
    base_url="https://openrouter.ai/api/v1", api_key=os.getenv("OPENAI_API_KEY")
)
BEFORE_PROMPT = "Your only task is to generate valid BPMN 2.0 XML diagrams compatible with the BPMN.js library. The XML must include both the process definition and all required graphical information (BPMNDiagram, BPMNPlane, shapes, and edges). Return only the raw XML without any explanation or comments."
