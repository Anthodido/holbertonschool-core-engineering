#!/usr/bin/env python3
"""WebSocket server that validates incoming messages before echoing them."""
import asyncio
import websockets
from websockets.exceptions import ConnectionClosed


async def connection_handler(websocket):
    """Reject empty/whitespace-only messages, otherwise echo with OK: prefix."""
    try:
        async for message in websocket:
            if len(message.strip()) == 0:
                await websocket.send("ERR:EMPTY")
            else:
                await websocket.send(f"OK:{message}")
    except ConnectionClosed:
        pass


async def main():
    async with websockets.serve(connection_handler, "localhost", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
