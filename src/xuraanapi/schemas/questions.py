from typing import List
from pydantic import UUID4, BaseModel


class LocalizedQuestion(BaseModel):
    question_id: UUID4
    text: str

    class Config:
        orm_mode = True    

class QuestionCreate(BaseModel):
    id: UUID4
    text: List[LocalizedQuestion]


class QuestionOut(BaseModel):
    id: UUID4
    text: str



class QuestionIn(BaseModel):
    id: UUID4  #version id
    language: str
