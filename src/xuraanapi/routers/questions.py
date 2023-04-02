from typing import List, Union
from fastapi import APIRouter, Depends

from ..schemas.questions import QuestionOut


from ..deps import get_db
from ..schemas.versions import VersionOut
from ..models import LocalizedQuestion, Question, Version, VersionDescription
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/questions",
    tags=["Questions"],
    responses={404: {"description": "Not found"}},
)


@router.get("")
async def get_questions(language: str = "en", db: Session = Depends(get_db)):
    # Join the Version and VersionDescription tables and filter by language
    questions = db.query(Question.id, LocalizedQuestion.text).join(LocalizedQuestion).filter(LocalizedQuestion.language == language ).all()

    return [QuestionOut(id=question_id, text=text) for question_id, text in questions]
