from fastapi import FastAPI
from app.interfaces.api.routes import image

app = FastAPI()

app.include_router(image.router)
