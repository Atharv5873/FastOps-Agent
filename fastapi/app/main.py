from fastapi import FastAPI
from .api import monitor

app= FastAPI(title="FastOps Agent API")

app.include_router(monitor.router, prefix="/monitor", tags=["monitor"])

@app.get("/")
async def root():
    return {"status": "ok", "service": "FastOps Agent API Running"}