import logging
import os
import MetaTrader5 as mt5
from dotenv import load_dotenv
load_dotenv()

account = os.getenv('ACCOUNT_ID')
server= os.getenv('SERVER')
broker = os.getenv('BROKER')
password = os.getenv('PASSWORD')
account = int(account)

print(type(account))

if account is None or server is None or broker is None or password is None:
    logging.error("Env variables not set")
    raise ValueError("Env variable not set")

# Initialize the MetaTrader 5 connection
def init_mt5():
    if not mt5.initialize():
        logging.error(f"Failed to init mt5 {mt5.last_error()}")
    if mt5.login(account_number=account,password=password):
        logging.info(f"Logged in with {account}")
    else:
        logging.error(f"Failed to log in with the error {mt5.last_error()}")
    mt5.shutdown()
