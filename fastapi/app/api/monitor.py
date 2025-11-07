from fastapi import APIRouter, HTTPException, Header
from datetime import datetime
from ..schemas import MetricPayload
from ..db.mongo_client import metrics

router = APIRouter()

@router.post("/ingest")
async def ingest_metric(payload: MetricPayload, x_api_key: str = Header(None)):
    if x_api_key != "devkey":
        raise HTTPException(status_code=403, detail="Forbidden")
    
    doc = payload.dict()
    doc["received_at"] = datetime.utcnow()
    await metrics.insert_one(doc)
    return {"status": "ok", "inserted": True}

@router.get("/latest/{server_id}")
async def get_latest(serveer_id: str):
    doc = await metrics.find_one(
        {"server_id": serveer_id},
        sort=[("timestamp", -1)]
    )
    if not doc:
        raise HTTPException(status_code=404, detail="Not Found")
    doc["_id"] = str(doc["_id"])
    return doc