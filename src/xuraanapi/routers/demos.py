from typing import List
from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from .database import demos

router = APIRouter(
    prefix="/demos",
    tags=["Demos"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
def get_demo_image(name: str):
    res = demos.get(name)
    media_type = name.split('.')[-1]
    return StreamingResponse(res.iter_chunks(1024), media_type=f"image/{media_type}")
