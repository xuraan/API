from typing import List, Union
from fastapi import APIRouter, Depends

from ..schemas.answers import AnswerIn, AnswerOut


from ..deps import get_db
from ..schemas.versions import VersionOut
from ..models import LocalizedQuestion, Answer, Version, LocalizedAnswer
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/answers",
    tags=["Answers"],
    responses={404: {"description": "Not found"}},
)


@router.get("")
async def get_answers(id: str, language: str, db: Session = Depends(get_db)):
    # Join the Version and VersionDescription tables and filter by language
    ans = db.query(Answer.id, Answer.src, LocalizedAnswer.text).join(LocalizedAnswer).filter(LocalizedAnswer.language == language, Answer.id == id ).first()
    return AnswerOut(id=ans[0], text=ans[2], src=ans[1])
