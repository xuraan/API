from typing import List
from fastapi.middleware.cors import CORSMiddleware

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from xuraanapi import models
from db.database import SessionLocal, engine

from xuraanapi.routers.versions import router as versions_router
from xuraanapi.routers.locals import router as locals_router
from xuraanapi.routers.questions import router as questions_router
from xuraanapi.routers.answers import router as ans_router


models.Base.metadata.create_all(bind=engine)

app = FastAPI(title = "XuraanAPI", docs_url="/")

# configure CORS
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
9
app.include_router(versions_router)
app.include_router(questions_router)
app.include_router(ans_router)
app.include_router(locals_router)










