from typing import List
from fastapi import APIRouter, Depends

from xuraanapi.provider.locals import get_localized_strings


from ..deps import get_db
from ..models import Local
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/locals",
    tags=["Locals"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def all(db: Session = Depends(get_db)):
    return db.query(Local).all()

    
@router.get("/localized")
async def localized_strings(language: str):
    return get_localized_strings(language)
    