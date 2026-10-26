from pydantic import BaseModel

class DeviceData(BaseModel):
    name : str
    metrics_data: MetricsData
    discord_data: DiscordData | None = None

class MetricsData(BaseModel):
    cpu_temp: float
    cpu_usage: float
    gpu_temp: float
    gpu_usage: float
    ram_usage: float

class DiscordData(BaseModel):
    muted: bool
    deafened: bool