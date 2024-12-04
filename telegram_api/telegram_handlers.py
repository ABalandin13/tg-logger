from telethon import events, Client

from utils.logger import logger


async def add_events(client: Client):
    logger.info(f"Add events handler")
    client.add_event_handler(new_message, events.NewMessage)
    client.add_event_handler(delete_message, events.MessageDeleted)
    client.add_event_handler(edited_message, events.MessageEdited)


async def new_message(message: events.NewMessage):
    logger.info(f'Message Id : {message.id} Text: {message.text[:50]}...')


async def delete_message(message: events.MessageDeleted):
    logger.info(f'Messages Id : {message.message_ids} Delete')


async def edited_message(message: events.MessageEdited):
    logger.info(f'Message Id : {message.id} Edited')
