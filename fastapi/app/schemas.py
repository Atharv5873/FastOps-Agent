from pydantic import BaseModel
from typing import Dict, Any

class MetricPayload(BaseModel):
    server_id: str
    timestamp: float
    cpu_percent: float
    mem_used: float
    mem_total: float
    disk_used: float
    disk_total: float
    containers: Dict[str, Any] = {}
