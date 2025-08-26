from langchain_google_genai import ChatGoogleGenerativeAI
from prompt_templates import welcome_user_prompt, random_generation_prompt
from models import WelcomeResponse, GenerationResponse
from os import getenv


class Agent:

    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model=getenv("GEMINI_MODEL"),
            temperature=0.7,
            google_api_key=getenv("GEMINI_API_KEY"),

        )

    def welcome_user(self):
        return self.llm.with_structured_output(WelcomeResponse).invoke(welcome_user_prompt.format_messages())

    def generate_random_json(self, num: int, category: str):
        return self.llm.with_structured_output(GenerationResponse).invoke(random_generation_prompt.format_messages(num=num, category=category))
