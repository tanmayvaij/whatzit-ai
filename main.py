from fastapi import FastAPI
from dotenv import load_dotenv
from os import getenv
from typing import List

from prompts import (
    WELCOME_USER_PROMPT,
    RANDOM_GENERATION_PROMPT,
    CUSTOM_GENERATION_PROMPT,
)
from models import WelcomeResponse, GenerationResponse
from genai import ask_gemini

load_dotenv()

GEMINI_MODEL = getenv("GEMINI_MODEL")
GEMINI_API_KEY = getenv("GEMINI_API_KEY")

if (GEMINI_MODEL is None) or (GEMINI_API_KEY is None):
    raise ValueError(
        "GEMINI_MODEL and GEMINI_API_KEY environment variables are not set"
    )

app = FastAPI(title="Whatzit AI")


@app.get(
    "/", response_model=WelcomeResponse, summary="An entry point in the WhatzIt AI"
)
def hello():
    return ask_gemini(WELCOME_USER_PROMPT)


@app.get(
    "/generate/sample",
    response_model=List[GenerationResponse],
    summary="Data generation",
)
def generate(category: str, num: int = 8):
    return ask_gemini(RANDOM_GENERATION_PROMPT.format(num=num, category=category))


@app.get("/generate/custom")
def generate_custom(requirement: str):
    return ask_gemini(CUSTOM_GENERATION_PROMPT.format(requirement=requirement))
