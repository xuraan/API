"""
Module to manage endpoints related to quranApp versions (version number and description).

This module defines an API router for endpoints related to quranApp version (version number and description). The router includes two endpoint handlers:
- '/versions/{local}': Retrieves all versions (version number and description) of quranApp in a given language.
- '/versions/': Retrieves all versions (version number and description) of quranApp in the default language ("en").

Usage:
- Import the 'router' object from this module to add version-related endpoints to your FastAPI application.

Example usage:
    from fastapi import FastAPI
    from package_name.routers import versions
    
    app = FastAPI()
    
    app.include_router(versions.router)

"""

from fastapi import APIRouter
from .database import en_versions, ar_versions, fr_versions
from typing import List

router = APIRouter(
    prefix="/versions",
    tags=["Versions"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def all(local: str = "en") -> List[dict]:
    """
        Retrieves all versions (version number and description) of quranApp in a given language.

        Parameters:
        - `local: str` The language to retrieve versions (version number and description) for. Defaults to "en" if not specified.

        Returns:
        - `List[Version]` A list of all versions (version number and description) in the given language.
    """
    return (fr_versions if local == "fr" else ar_versions if local == "ar" else en_versions).fetch().items
