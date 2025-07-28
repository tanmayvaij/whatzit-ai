from langchain_google_genai import GoogleGenerativeAI
from prompt_templates import welcome_user_prompt, random_generation_prompt
from os import getenv


class Agent:

    def __init__(self):
        self.llm = GoogleGenerativeAI(
            model=getenv("GEMINI_MODEL"),
            temperature=0.7,
            google_api_key=getenv("GEMINI_API_KEY"),
        )

    def welcome_user(self):
        return self.llm.invoke(welcome_user_prompt.format())

    def generate_random_json(self, num: int, category: str):
        return self.llm.invoke(
            random_generation_prompt.format(num=num, category=category)
        )
