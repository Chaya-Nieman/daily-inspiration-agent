"""
agent.py

Configures and runs the Daily Inspiration Agent using the OpenAI Agents SDK
with Google Gemini as the model provider via the OpenAI-compatible endpoint.
"""

import os
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel

# The agent's persona and instructions
AGENT_INSTRUCTIONS = """
You create beautiful daily inspiration emails in English.
Generate exactly one authentic quote from a famous thinker, philosopher, scientist, leader, or author.
Always include the author's name.
After the quote, write a short reflection (2–3 sentences) explaining how the wisdom can inspire someone's day.
Keep the tone uplifting, thoughtful, elegant, and encouraging.
Return only the inner HTML content suitable for an email body — specifically:
- A <blockquote> element containing the quote text
- A <p> element with the author's name styled with class "author"
- A <p> element with the reflection styled with class "reflection"
Do NOT return a full HTML page. Do NOT include <html>, <head>, <body>, or any wrapper tags.
Do NOT include markdown, code blocks, or any explanation. Only the HTML snippet.
"""


def create_agent() -> Agent:
    """
    Creates and returns the Daily Inspiration Agent configured to use
    Google Gemini via the OpenAI-compatible API endpoint.
    """
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY is not set in environment variables.")

    # Configure the Gemini endpoint using OpenAI-compatible client
    # Google AI Studio exposes a Gemini endpoint compatible with the OpenAI SDK
    gemini_client = AsyncOpenAI(
        api_key=api_key,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    )

    # Use gemini-2.5-flash — latest model with best quota availability
    model = OpenAIChatCompletionsModel(
        model="gemini-2.5-flash",
        openai_client=gemini_client,
    )

    agent = Agent(
        name="Daily Inspiration Agent",
        instructions=AGENT_INSTRUCTIONS,
        model=model,
    )

    return agent


async def generate_inspiration() -> str:
    """
    Runs the agent and returns the generated HTML content snippet.
    """
    agent = create_agent()

    result = await Runner.run(
        agent,
        input="Generate today's inspirational email content.",
    )

    return result.final_output
