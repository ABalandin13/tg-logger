from telethon import Client

from utils.logger import logger


async def search_old_messages(client: Client):
    async for message in client.search_all_messages(limit=5):
        if message.sender:
            logger.info(f'Id: {message.id} Sender id: {message.sender.id} Text: {message.text[:50]}...')
        elif message.chat:
            logger.info(f'Id:{message.id} Chat id:{message.chat.id} Text: {message.text[:50]}...')