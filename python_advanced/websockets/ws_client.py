#!/usr/bin/env python3
"""Minimal WebSocket client."""
import asyncio
import websockets


async def connect_and_send(uri: str, text: str, deadline: float = 15.0, delay: float = 0.3) -> str:
    """Send text over uri and return the single response received.

    Retries the initial connection to tolerate a server that has not
    finished starting up yet.
    """
    loop = asyncio.get_event_loop()
    start = loop.time()
    while True:
        try:
            async with websockets.connect(uri) as websocket:
                await websocket.send(text)
                return await websocket.recv()
        except OSError:
            if loop.time() - start >= deadline:
                raise
            await asyncio.sleep(delay)


async def main():
    response = await connect_and_send("ws://localhost:8765", "demo")
    print(response, end="")


if __name__ == "__main__":
    asyncio.run(main())
