from loader import bot, storage
import os
import redis
import sqlite3

os.system('redis-server /etc/redis/6379.conf')
redis_control = redis.Redis()
db = sqlite3.connect('Words_Data_Base.db')


# "on_shutdown" function that called at the end of bot


async def on_shutdown(dp):
    await bot.close()
    await storage.close()
    os.system('redis-cli shutdown')
    db.close()


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_shutdown=on_shutdown)
