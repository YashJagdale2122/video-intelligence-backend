from fastapi import FastAPI
from app.api.routes import videos

app = FastAPI (title = "Video Intelligence Backend", version="1.0.0")

app.include_router(videos.router)

@app.get("/api/v1/health")
def health_check():
    return {"status" : "Ok"}
