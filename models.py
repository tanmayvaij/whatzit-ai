from pydantic import BaseModel


class WelcomeResponse(BaseModel):
    message: str


class GenerationResponse(BaseModel):
    id: str
    name: str
    description: str
