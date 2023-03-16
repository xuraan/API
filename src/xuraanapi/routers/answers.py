from typing import List, Union
from fastapi import APIRouter

from .database import ar_questions, en_features, en_answers, fr_answers, ar_answers


router = APIRouter(
    prefix="/answers",
    tags=["Answers"],
    responses={404: {"description": "Not found"}},
)


@router.get("/{question_id}")
async def answer(question_id: str, local: str = "en") -> Union[dict, None]:
    res = (fr_answers if local == "fr" else ar_answers if local == "ar" else en_answers).get(question_id)
    
    return res

@router.get("/")
async def all(local: str = "en") -> List[dict]:
    return (fr_answers if local == "fr" else ar_answers if local == "ar" else en_answers).fetch().items
