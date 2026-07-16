#!/usr/bin/env python3
"""WebSocket server that broadcasts every message to all connected clients."""
import asyncio
import websockets
from websockets.exceptions import ConnectionClosed

connected_clients = set()


async def connection_handler(websocket):
    """Track the connection and broadcast each message, prefixed with B:."""
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            websockets.broadcast(connected_clients, f"B:{message}")
    except ConnectionClosed:
        pass
    finally:
        connected_clients.discard(websocket)


async def main():
    async with websockets.serve(connection_handler, "localhost", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
