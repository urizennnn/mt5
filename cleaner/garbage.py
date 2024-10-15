import glob
import os

from telethon.sync import asyncio

async def clean_media_after_timeout():
    for file in glob.glob("media/*"):
        await asyncio.sleep(5)
        os.remove(file)
