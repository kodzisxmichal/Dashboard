from fastapi import FastAPI
from app.routes import router
from app.hub import hub_router

app = FastAPI()

app.include_router(router)
app.include_router(hub_router)
