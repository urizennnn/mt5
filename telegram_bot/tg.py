import os
from telethon.sync import TelegramClient
from telethon.tl.types import Channel, Chat,  TypeInputPeer
from dotenv import load_dotenv

from telegram_bot.image_reader import read_image

load_dotenv()

api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
phone = os.getenv('PHONE')
target_chan = "Vip signal gc💰💸"

if api_id is None or api_hash is None or phone is None:
    raise ValueError("API_ID, API_HASH, and PHONE must be set in the environment variables")

api_id = int(api_id)
phone = str(phone)

client = TelegramClient('TradingBot', api_id, api_hash)


async def start_client():
    await client.connect()

    if not await client.is_user_authorized():
        await client.send_code_request(phone)
        await client.sign_in(phone, input('Enter the code: '))

    value = await get_chan()
    channel = await client.get_input_entity(value)

    while True:  # Infinite loop
        async for message in client.iter_messages(channel, limit=3):
            if message.media:
                file_path = await message.download_media(file=os.path.join(os.getcwd(), "media"))
                image= read_image(file_path)
                print(image)
            else:
                print(f"Message: {message.message}")


async def get_chan() -> TypeInputPeer:
    dialogs = await client.get_dialogs()

    for dialog in dialogs:
        if isinstance(dialog.entity, (Channel, Chat)):
            if dialog.name == target_chan:
                return await client.get_input_entity(dialog.entity)

    raise ValueError(f"Channel {target_chan} not found")


