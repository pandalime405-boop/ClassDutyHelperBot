import asyncio
from aiogram import Bot

TOKEN = "8354172231:AAEq2OuXq45Klg3ekYa1CNS8spqYRhbwGac"
CHAT_ID = -4998505111  # твоє CHAT_ID

async def test_message():
    bot = Bot(token=TOKEN)
    await bot.send_message(CHAT_ID, "✅ Тестове повідомлення: бот працює!")
    await bot.close()

if __name__ == "__main__":
    asyncio.run(test_message())
