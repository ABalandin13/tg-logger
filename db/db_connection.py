import os
import psycopg2

from utils.logger import logger

DATABASE_URL = os.getenv('DATABASE_URL')

conn = None

def get_connection():
    global conn

    logger.info(f"Get DB connection")
    if conn is None:
        conn = psycopg2.connect(DATABASE_URL)
        return conn

    return conn