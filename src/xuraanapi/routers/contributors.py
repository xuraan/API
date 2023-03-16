from typing import List
from fastapi import APIRouter

from .database import contributors

router = APIRouter(
    prefix="/contributors",
    tags=["Contributors"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def all() -> List[dict]:
    return contributors.fetch().items
