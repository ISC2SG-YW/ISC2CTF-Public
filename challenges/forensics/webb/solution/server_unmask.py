#!/usr/bin/env python

import asyncio

from websockets.server import serve
import json

async def serv(websocket):
    start = False
    i = 0
    async for message in websocket:
        if message == json.dumps({"info": "TRANSMISSION COMPLETE"}):
            print(message)
            print("EXITING")
            exit()
        if message == json.dumps({"info": "SERVER UP"}):
            start = True
            await websocket.send(json.dumps({"cmd":"./retreive_data --codename=WEBB -l"}))
        if start:
            await websocket.send(json.dumps({"cmd":f"./retreive_data --codename=WEBB -i {i}"}))
            i += 1

async def main():
    async with serve(serv, "localhost", 8765, compression=None):
        await asyncio.Future()  # run forever

asyncio.run(main())
