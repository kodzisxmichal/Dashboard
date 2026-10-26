from fastapi import APIRouter
from .state import DeviceDataPacket, devices
from .models import DeviceData
from .watchdog import feed_watchdog
from .hub import broadcast

router = APIRouter()

@router.get("/metrics")
async def get_metrics():
    return devices

@router.post("/metrics/{id}")
async def receive_metrics(id, data: DeviceData):
    devices[id] = DeviceDataPacket(device_data=data)
    feed_watchdog(id)
    await broadcast()
    return 0
