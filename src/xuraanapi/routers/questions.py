from typing import List
from fastapi import APIRouter

from .database import fr_questions, ar_questions, en_questions

router = APIRouter(
    prefix="/questions",
    tags=["Questions"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def all(local: str = "en") -> List[dict]:
    return (fr_questions if local == "fr" else ar_questions if local == "ar" else en_questions).fetch().items