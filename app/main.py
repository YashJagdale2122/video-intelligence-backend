from fastapi import FastAPI
from app.api.routes import videos,health
from app.core.database import engine, Base
app = FastAPI (title = "Video Intelligence Backend", version="1.0.0")

app.include_router(videos.router)
app.include_router(health.router, tags=["Health"])
