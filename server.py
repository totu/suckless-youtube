#!/usr/bin/env python3

import asyncio
import websockets
import youtube_dl

async def get_vid(websocket, path):
    del path

    video_url = await websocket.recv()
    opts = {"outtmpl": "vids/%(title)s.%(ext)s"}

    with youtube_dl.YoutubeDL(opts) as ydl:
        ydl.download([video_url])

# Serving
start_server = websockets.serve(get_vid, "localhost", 5555)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
