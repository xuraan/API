from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import routers

from routers.answers import router as a_router
from routers.avatars import router as av_router
from routers.contributors import router as c_router
from routers.demos import router as d_router
from routers.features import router as f_router
from routers.locals import router as l_router
from routers.questions import router as q_router
from routers.versions import router as v_router

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

app.include_router(a_router)
app.include_router(av_router)
app.include_router(c_router)
app.include_router(d_router)
app.include_router(f_router)
app.include_router(l_router)
app.include_router(q_router)
app.include_router(v_router)
