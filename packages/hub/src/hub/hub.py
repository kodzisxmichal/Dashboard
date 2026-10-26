from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from .state import devices

hub_router = APIRouter()
clients = set()                   # pusty set

def state_as_dict():
    state = {}
    for device_id, packet in devices.items():
        state[device_id] = packet.model_dump(mode="json")
    return state
    
@hub_router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.add(websocket)
    # 2. wyślij temu jednemu klientowi pełny stan (send_json + state_as_dict)
    await websocket.send_json(state_as_dict())
    # 3. try: pętla while True z receive_text()
    #    except WebSocketDisconnect: usuń websocket z clients (discard)
    while True:
        try:
            await websocket.receive_text()
        except WebSocketDisconnect:
            clients.discard(websocket)
            return

async def broadcast():
    # 1. raz zbuduj pełny stan (state_as_dict)
    payload = state_as_dict()
    # 2. pętla po KOPII zbioru: for ws in list(clients)
    for ws in list(clients):
        try:
            await ws.send_json(payload)
        except Exception:
            clients.discard(ws)

    #       try: wyślij stan do ws
    #       except Exception: usuń ws z clients
