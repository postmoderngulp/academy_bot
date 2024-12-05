import asyncio
from aiogram import Bot, Dispatcher
from telegram_bot.user_handlers import userRouter
from telegram_bot.admin_handlers import adminRouter
from telegram_bot.employee_handlers import employeeRouter

from database.models import async_main


    
async def main():
    await async_main()
    bot = Bot(token='7904510825:AAFprv0Q2TAm6_H2gSh8d0gTCmV5QSAn2zc')
    dp = Dispatcher()
    dp.include_routers(userRouter,employeeRouter,adminRouter)
    await dp.start_polling(bot)
    


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('bot is turned off')