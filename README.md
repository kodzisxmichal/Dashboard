# Dashboard

A home project for watching my PC and home server on an ESP32 with an OLED screen. I'm also using it to learn FastAPI.

A small program on each machine sends temperatures and usage to a central server (the hub). The hub pushes the latest numbers to the ESP32 over a WebSocket.

## Status

The hub works. The agent that runs on each machine, the Discord mute and the ESP32 code are not done yet.

## Running the hub

You need uv. From the repository root:

```
uv sync
uv run --package hub fastapi dev packages/hub/src/hub/main.py
```

Then open http://127.0.0.1:8000/docs.

## How the hub works

- `POST /metrics/{id}` receives the readings of one device
- `GET /metrics` returns everything
- `/ws` is the WebSocket for the ESP32, it gets the full state on connect and on every change
- a device that sends nothing for 30 seconds is marked as offline
