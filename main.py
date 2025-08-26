from fastapi import FastAPI
from dotenv import load_dotenv
from os import getenv
from typing import List
from models import WelcomeResponse, GenerationResponse
from agent import Agent
from json import loads

load_dotenv()

GEMINI_MODEL = getenv("GEMINI_MODEL")
GEMINI_API_KEY = getenv("GEMINI_API_KEY")

if (GEMINI_MODEL is None) or (GEMINI_API_KEY is None):
    raise ValueError(
        "GEMINI_MODEL and GEMINI_API_KEY environment variables are not set"
    )

app = FastAPI(title="Whatzit AI")


agent = Agent()


@app.get(
    "/", response_model=WelcomeResponse, summary="An entry point in the WhatzIt AI"
)
def welcome_user():
    return agent.welcome_user()


@app.get(
    "/generate/sample",
    response_model=List[GenerationResponse],
    summary="Data generation",
)
def generate_random_json(category: str, num: int = 8):
    return loads(agent.generate_random_json(num, category))
