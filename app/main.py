from fastapi import FastAPI
from app.api.routes import translation

app = FastAPI()

app.include_router(translation.router, prefix="/translate", tags=["Translation"])
