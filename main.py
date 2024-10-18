import logging
import tracemalloc
from dotenv import load_dotenv
from MT5.bot import init_mt5
import MetaTrader5 as mt5
from cleaner.garbage import clean_media_after_timeout
from telegram_bot.tg import start_client, client

tracemalloc.start()
load_dotenv()

async def main():
    logging.basicConfig(level=logging.INFO)
    logging.info("Starting the bot")

    try:
        # await start_client()
        init_mt5()
        await clean_media_after_timeout()
    except KeyboardInterrupt:
        logging.info("Interrupted. Cleaning up media before exiting...")
    finally:
        await clean_media_after_timeout()  

if __name__ == "__main__":
    with client:  # Starts the client and keeps the context
        client.loop.run_until_complete(main())

