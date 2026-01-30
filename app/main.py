from fastapi import FastAPI
from app.api.routes import videos
from app.core.database import engine, Base
app = FastAPI (title = "Video Intelligence Backend", version="1.0.0")

app.include_router(videos.router)

@app.get("/api/v1/health")
def health_check():
    return {"status" : "Ok"}

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)
