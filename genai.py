from os import getenv
from json import loads
from fastapi import HTTPException
from google import genai


gemini_client = genai.Client()


def ask_gemini(prompt: str) -> dict:
    try:
        response = gemini_client.models.generate_content(
            model=getenv("GEMINI_MODEL"),
            contents=prompt,
            config={
                "system_instruction": "You are only a random data generation which will generate some random json array on user request"
            },
        )

        return loads(response.text)
    except HTTPException as e:
        raise HTTPException(500, str(e))
