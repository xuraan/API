from typing import List
from pydantic import BaseModel


class VersionDescribtion(BaseModel):
    version_id: str
    description: str

    class Config:
        orm_mode = True    

class VersionCreate(BaseModel):
    id: int
    description: List[VersionDescribtion]


class VersionOut(BaseModel):
    id: str
    description: str



class VersionIn(BaseModel):
    id: str  #version id
    language: str
