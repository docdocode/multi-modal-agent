from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.tavily import TavilyTools
from constants import SYSTEM_PROMPT, INSTRUCTIONS
from dotenv import load_dotenv
import os

load_dotenv()

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

agent = Agent(
    model = Gemini(),
    tools = [TavilyTools()],
    markdown = True,
    system_prompt = SYSTEM_PROMPT,
    instructions = INSTRUCTIONS
)

agent.print_response(
    "analyse this food image",
    # images = ['images/ramen.jpg'],
    images = ['https://i.redd.it/vjyiqbgf6xd11.jpg'],
    stream = True
)