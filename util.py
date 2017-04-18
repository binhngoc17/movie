from pymessenger.bot import Bot
import os

VERIFY_TOKEN = os.environ['VERIFY_TOKEN']
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
bot = Bot(ACCESS_TOKEN)