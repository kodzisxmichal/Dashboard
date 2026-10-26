import asyncio
from .state import DeviceDataPacket, devices
from .hub import broadcast

countdown_timer = {}
OFFLINE_TIMEOUT = 30

async def mark_offline_after(device_id, sleep_time):
    await asyncio.sleep(sleep_time)
    packet: DeviceDataPacket = devices.get(device_id)
    packet.is_online = False
    await broadcast()

def feed_watchdog(device_id):
    if(countdown_timer.get(device_id) != None):
        timer: asyncio.Task = countdown_timer[device_id]
        timer.cancel()
    
    countdown_timer[device_id] = asyncio.create_task(mark_offline_after(device_id, OFFLINE_TIMEOUT))
    return