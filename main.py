from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
from google import genai
from json import loads
from os import getenv

load_dotenv()

GEMINI_MODEL = getenv("GEMINI_MODEL")

app = FastAPI(title="Whatzit AI")

gemini_client = genai.Client()

WELCOME_USER_PROMPT = """
YOU ARE A GREETER of the WHATZIT AI ( a random data generator AI system ), 
who has only one job to greet user and define your purpose.

the response should be ##strictly and only in a plain text##,
the required python dictionary schema is given below

{ message: <your-long-welcome-message> }

##strictly, no code blocks, markdown or commentary## should be given in the response
"""

RANDOM_GENERATION_PROMPT = """
YOU ARE A RANDOM DATA GENERATOR, you need to generate the list of N number of objects of a particular CATEGORY

So generate a python list of {num} objects of {category}

the response should be ##strictly and only in plain text##,
the type of required python dictionary schema of an object of the list is given below

{{ 
    id: <uuidv4>,
    name: <product-name>,
    description: <a-short-description-of-the-product>,
}}

##strictly, no code blocks, markdown or commentary## should be given in the response
"""


class WelcomeResponse(BaseModel):
    message: str


class GenerationRequest(BaseModel):
    num: int = 8
    category: str


def ask_gemini(prompt: str) -> dict:
    try:
        response = gemini_client.models.generate_content(
            model=GEMINI_MODEL, contents=prompt
        )
        print(response.text)
        return loads(response.text)
    except HTTPException as e:
        raise HTTPException(500, str(e))


@app.get(
    "/", response_model=WelcomeResponse, summary="An entry point in the WhatzIt AI"
)
def hello():
    return ask_gemini(WELCOME_USER_PROMPT)


@app.get("/generate", summary="Data generation")
def generate(category: str, num: int = 8):
    return ask_gemini(RANDOM_GENERATION_PROMPT.format(num=num, category=category))
