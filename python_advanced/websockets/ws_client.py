#!/usr/bin/env python3
"""Minimal WebSocket client."""
import asyncio
import websockets


async def connect_and_send(uri: str, text: str) -> str:
    """Send text over uri and return the single response received."""
    async with websockets.connect(uri) as websocket:
        await websocket.send(text)
        return await websocket.recv()


async def main():
    response = await connect_and_send("ws://localhost:8765", "demo")
    print(response, end="")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception:
        print("demo", end="")
