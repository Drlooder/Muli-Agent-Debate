from openai import OpenAI
import os
from dotenv import load_dotenv
import Services.config as config

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
    text_to = text + f" | note: {config.AGENTS_PROMPTS.get(agent) or "Nevermind "} "
    response = client.responses.create(
        input=text_to,
        model="openai/gpt-oss-20b"
    )

    return response.output_text


def get_random_topic():
    return client.responses.create(
        input="Generate one interesting debate topic. Return only the topic and nothing else.",
        model="openai/gpt-oss-20b"
    ).output_text