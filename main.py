import asyncio
from aiogram import Bot, Dispatcher
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime

TOKEN = "8354172231:AAEq2OuXq45Klg3ekYa1CNS8spqYRhbwGac"
CHAT_ID = -1001234567890  # id класної бесіди

students = [
    "Андрусик Ангеліна",
    ".Болюк Денис",
    "Ватаг Руслан",
    "Веселик Оксана",
    "Візнюк Назар",
    "Добровольський Артем",
    "Іванченко Давид",
    "Їжак Софія",
    "Ковальов Кирило",
    "Костишин Аліна",
    "Косаренко Марта",
    "Кіяшко Роман",
    "Курилишин Вероніка",
    "Мисак Тарас",
    "Мартинчук Нікіта",
    "Проців Захар",
    "Сорочинська Софія",
    "Стасула Настя",
    "Сеньків Максим",
    "Ткачишин Марта",
    "Феденяк Маргарита",
    "Феделеш Юрій",
    "Яцик Данило",
    "Яцура Матвій"
    
    
]

index = 0  # початок циклу


async def send_duty():
    global index
    bot = Bot(token=TOKEN)

    # беремо 2 учнів зі списку по черзі
    duty = [students[index % len(students)], students[(index + 1) % len(students)]]
    index += 2

    text = f"Чергові: {duty[0]}, {duty[1]}"

    await bot.send_message(CHAT_ID, text)
    await bot.session.close()


async def main():
    dp = Dispatcher()

    scheduler = AsyncIOScheduler(timezone="Europe/Kyiv")

    scheduler.add_job(
        send_duty,
        trigger="cron",
        day_of_week="mon-fri",
        hour=8,
        minute=20
    )

    scheduler.start()
    await dp.start_polling(Bot(TOKEN))


if __name__ == "__main__":
    asyncio.run(main())
