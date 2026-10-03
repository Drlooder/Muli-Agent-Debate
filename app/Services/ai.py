from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.environ.get("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

def generate_response(text: str, agent: str) -> str:
    """ 
    Generating a response from The ai.

    Returning clean **STR** from the ai
    """

    response = client.responses.create(
        input=text,
        model="openai/gpt-oss-20b"
    )

    return response.output_text