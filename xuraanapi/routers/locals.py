from typing import List
from fastapi import APIRouter

from .database import locals, localized_strings_dict

router = APIRouter(
    prefix="/locals",
    tags=["Locals"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def all() -> List[dict]:
    return locals.fetch().items

@router.get("/{key}")
async def localized_strings(key: str) -> dict:
    return locals.get(key)
    
@router.get("/{key}/localized_strings_dict")
async def localized_strings(key: str) -> dict:
    strings_dict = localized_strings_dict.get(key)
    try:
        return strings_dict['strings']
    except:
        return {}