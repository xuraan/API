from typing import List
from pydantic import BaseModel


class LocalizedQuestion(BaseModel):
    question_id: str
    text: str

    class Config:
        orm_mode = True    

class QuestionCreate(BaseModel):
    id: str
    text: List[LocalizedQuestion]


class QuestionOut(BaseModel):
    id: str
    text: str



class QuestionIn(BaseModel):
    id: str  #version id
    language: str
