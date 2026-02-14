import os
from openai import OpenAI
from pydantic import BaseModel
from googletrans import Translator
from googletrans import LANGUAGES
import json

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

system_prompt = """
You are a professional summarization assistant.

Rules:
- The summary must be written in English.
- Minimum 30 words.
- Maximum 200 words.
- Do not add explanations.
- Only return the summary.
"""


def run_agent(user_text):

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_text}
    ]

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
    )

    message = response.choices[0].message

    return message.content
