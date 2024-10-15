import logging
import tracemalloc
from dotenv import load_dotenv
from telegram_bot.tg import start_client, client 

tracemalloc.start()
load_dotenv()

async def main():
    logging.basicConfig(level=logging.INFO)
    logging.info("Starting the bot")
    await start_client()

if __name__ == "__main__":
    with client:
        client.loop.run_until_complete(main())
