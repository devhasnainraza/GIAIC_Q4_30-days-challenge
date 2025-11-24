import os
from dotenv import load_dotenv
from agents import Agent, OpenAIChatCompletionsModel
from openai import AsyncOpenAI
from tools import read_user_profile, update_user_profile

load_dotenv()

# Get the API key from the environment
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Check if the API key is available
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY not found in environment variables.")

# Initialize the Gemini client
gemini_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# Initialize the Gemini model
gemini_model = OpenAIChatCompletionsModel(
    model="gemini-2.5-pro",
    openai_client=gemini_client,
)

# Define the system prompt
system_prompt = "Greet users by name if known. Detect when users share personal info and save it using tools."

# Create the agent
agent = Agent(
    name="chatbot",
    instructions=system_prompt,
    tools=[read_user_profile, update_user_profile],
    model=gemini_model,
)
