from typing import List
from pydantic import BaseModel


class LocalizedAnswer(BaseModel):
    answer_id: str
    text: str

    class Config:
        orm_mode = True    

class AnswerCreate(BaseModel):
    id: str
    text: List[LocalizedAnswer]


class AnswerOut(BaseModel):
    id: str
    text: str
    src: str



class AnswerIn(BaseModel):
    id: str  #version id
    language: str
