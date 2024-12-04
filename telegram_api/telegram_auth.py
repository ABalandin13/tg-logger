import asyncio
import getpass
from dotenv import load_dotenv
import os

from telethon import Client
from telethon.types import User
from db.user_entity import wait_for_code, UserEntity
from utils.logger import logger

login_token = None

load_dotenv()

API_HASH = os.getenv('API_HASH')
API_ID = os.getenv('API_ID')


async def authenticate_user(user: UserEntity) -> Client:
    global login_token
    logger.info(f"Trying to authenticate user: {user.phone_number}")

    client = Client(user.session_name, int(API_ID), API_HASH)

    await client.connect()

    if not await client.is_authorized():
        await asyncio.sleep(30)
        logger.info(f"User with phone {user.phone_number} is not authorized, attempting to sign in.")
        phone = user.phone_number

        if login_token is None or not user.is_code_send:
            logger.info(f"Requesting login code for {phone}")
            login_token = await client.request_login_code(phone)
            user.is_code_send = True

        if not user.code:
            logger.info(f"No login code found for {phone}. Waiting for code from the database...")
            await wait_for_code(user)
        else:
            logger.info(f"Using code {user.code} for login.")

        if login_token is not None and user.code is not None:
            user_or_token = await client.sign_in(login_token, user.code)

            if isinstance(user_or_token, User):
                logger.info(f"Successfully logged in as {user_or_token.first_name}")
                login_token = None
            else:
                password_token = user_or_token
                password = getpass.getpass("Enter your 2FA password: ")
                user = await client.check_password(password_token, password)
                logger.info(f"Logged in with 2FA as {user.first_name}")

    else:
        logger.info(f"User with phone {user.phone_number} is already authorized.")

    return client
