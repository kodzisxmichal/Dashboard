from datetime import datetime
from .models import DeviceData
from pydantic import *

class DeviceDataPacket(BaseModel):
    device_data: DeviceData 
    timestamp: datetime = Field(default_factory=datetime.now)
    is_online: bool = True

devices = {}