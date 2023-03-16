"""
Module to manage endpoints related to features of quranApp.

This module defines an API router for endpoints related to features of quranApp.
The router includes one endpoint handler:
- '/features': Retrieves all features available in quranApp.

Usage:
- Import the 'router' object from this module to add feature-related endpoints to main FastAPI app.

Example usage:
    from fastapi import FastAPI
    from package_name.routers import features
    
    app = FastAPI()
    
    app.include_router(features.router)

"""

from typing import List
from fastapi import APIRouter

from .database import fr_features, ar_features, en_features

router = APIRouter(
    prefix="/features",
    tags=["features"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def all(local: str = "en") -> List[dict]:
    """
        Retrieves all features (feature id and description) of quranApp in a given language.

        Parameters:
        - `local: str` The language to retrieve features (feature number and description) for. Defaults to "en" if not specified.

        Returns:
        - `List[Features]` A list of all features (feature number and description) in the given language.
    """
    return (fr_features if local == "fr" else ar_features if local == "ar" else en_features).fetch().items
