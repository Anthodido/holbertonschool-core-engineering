#!/usr/bin/env python3
"""Minimal WebSocket client."""
import asyncio
import websockets


async def connect_and_send(uri: str, text: str, retries: int = 10, delay: float = 0.5) -> str:
    """Send text over uri and return the single response received.

    Retries the initial connection to tolerate a server that has not
    finished starting up yet.
    """
    for attempt in range(retries):
        try:
            async with websockets.connect(uri) as websocket:
                await websocket.send(text)
                return await websocket.recv()
        except OSError:
            if attempt == retries - 1:
                raise
            await asyncio.sleep(delay)


async def main():
    response = await connect_and_send("ws://localhost:8765", "demo")
    print(response, end="")


if __name__ == "__main__":
    asyncio.run(main())
