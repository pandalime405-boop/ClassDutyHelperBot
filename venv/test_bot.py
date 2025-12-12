import asyncio
from aiogram import Bot

TOKEN = "8354172231:AAEq2OuXq45Klg3ekYa1CNS8spqYRhbwGac"
CHAT_ID = -1001234567890  # заміни на свій chat_id

students = [
    "Андрусик Ангеліна",
    "Болюк Денис",
    "Ватаг Руслан",
    "Веселик Оксана",
    # ... решта учнів
]

INDEX_FILE = "index.txt"

# Читаємо останній індекс або ставимо 0
import os
if os.path.exists(INDEX_FILE):
    with open(INDEX_FILE, "r") as f:
        index = int(f.read())
else:
    index = 0

async def test_send():
    global index
    duty = [
        students[index % len(students)],
        students[(index + 1) % len(students)]
    ]
    text = f"Тестові чергові: {duty[0]}, {duty[1]}"
    
    bot = Bot(token=TOKEN)
    await bot.send_message(CHAT_ID, text)
    await bot.session.close()
    
    # Збільшимо індекс для наступного разу
    index += 2
    with open(INDEX_FILE, "w") as f:
        f.write(str(index))

asyncio.run(test_send())
