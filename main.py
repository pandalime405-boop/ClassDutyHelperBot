import asyncio
from aiogram import Bot, Dispatcher
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import os

TOKEN = "8354172231:AAEq2OuXq45Klg3ekYa1CNS8spqYRhbwGac"
CHAT_ID = -1001234567890  # id класної бесіди

students = [
    "Андрусик Ангеліна",
    "Болюк Денис",
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

INDEX_FILE = "index.txt"

# Читаємо останній індекс або ставимо 0
if os.path.exists(INDEX_FILE):
    with open(INDEX_FILE, "r") as f:
        index = int(f.read())
else:
    index = 0


async def send_duty(bot: Bot):
    global index

    duty = [
        students[index % len(students)],
        students[(index + 1) % len(students)]
    ]
    index += 2

    text = f"Чергові: {duty[0]}, {duty[1]}"
    await bot.send_message(CHAT_ID, text)

    # Зберігаємо індекс у файл
    with open(INDEX_FILE, "w") as f:
        f.write(str(index))


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    scheduler = AsyncIOScheduler(timezone="Europe/Kyiv")
    scheduler.add_job(
        send_duty,
        trigger="cron",
        day_of_week="mon-fri",
        hour=8,
        minute=20,
        args=[bot]
    )
    scheduler.start()

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
