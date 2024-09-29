from decouple import config
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

token = config('TOKEN2')

bot = Bot(token=token)
dp = Dispatcher(bot=bot)
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)

admin = ['5060685213']


