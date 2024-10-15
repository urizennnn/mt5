import logging
import tracemalloc
from dotenv import load_dotenv
from cleaner.garbage import clean_media_after_timeout
from telegram_bot.tg import start_client, client 

tracemalloc.start()
load_dotenv()

async def main():
    logging.basicConfig(level=logging.INFO)
    logging.info("Starting the bot")
    try:
        await start_client()
        await clean_media_after_timeout()
    except KeyboardInterrupt:
        await clean_media_after_timeout()

if __name__ == "__main__":
    with client:
        client.loop.run_until_complete(main())
