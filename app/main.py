from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv()


from app.interfaces.api.routes import image, auth
from app.infrastructure.db.models.base import Base
from app.infrastructure.db.session import engine


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(image.router)
