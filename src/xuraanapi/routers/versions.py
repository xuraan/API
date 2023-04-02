from typing import List, Union
from fastapi import APIRouter, Depends


from ..deps import get_db
from ..schemas.versions import VersionOut
from ..models import Version, VersionDescription
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/versions",
    tags=["Versions"],
    responses={404: {"description": "Not found"}},
)


@router.get("", response_model=List[VersionOut])
async def get_versions(language: str = "en", db: Session = Depends(get_db)):
    # Join the Version and VersionDescription tables and filter by language
    versions = db.query(Version.id, VersionDescription.text)\
        .join(VersionDescription)\
        .filter(VersionDescription.language == language )\
        .all()

    return [VersionOut(id=version_id, description=description) for version_id, description in versions]
