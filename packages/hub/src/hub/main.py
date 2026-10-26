from fastapi import FastAPI
from .routes import router
from .hub import hub_router

app = FastAPI()

app.include_router(router)
app.include_router(hub_router)
