from os import getenv
from json import loads
from fastapi import HTTPException
from google import genai


gemini_client = genai.Client()


def ask_gemini(prompt: str) -> dict:
    try:
        response = gemini_client.models.generate_content(
            model=getenv("GEMINI_MODEL"), contents=prompt
        )

        print(response.text)

        return loads(response.text)
    except HTTPException as e:
        raise HTTPException(500, str(e))
