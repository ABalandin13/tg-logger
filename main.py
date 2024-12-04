import asyncio

from telethon import Client

from db.user_entity import get_users_from_db
from telegram_api.telegram_auth import authenticate_user
from telegram_api.telegram_handlers import add_events
from telegram_api.telegram_messages import search_old_messages
from utils.logger import logger

authenticated_users = {}

async def listen_for_new_users(poll_interval=10):
    while True:
        logger.info("Checking for new users...")
        users = await get_users_from_db()

        for user in users:
            if user.phone_number not in authenticated_users:
                authenticated_users[user.phone_number] = True
                asyncio.create_task(process_user(user))

        await asyncio.sleep(poll_interval)


async def process_user(user):
    print(f"Starting authentication for {user.phone_number}")
    client = await authenticate_user(user)
    if isinstance(client, Client):
        logger.info(f"Search messages for user {user.phone_number}")

        await asyncio.sleep(10)
        await add_events(client=client)

        asyncio.create_task(search_old_messages(client=client))

        await client.run_until_disconnected()


async def main():
    logger.info("Starting the Telegram bot and listening for new users.")
    await listen_for_new_users()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.warning("Bot stopped by the user")
