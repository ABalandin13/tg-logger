import asyncio
from psycopg2 import sql
from psycopg2.extras import RealDictCursor
from db.db_connection import get_connection
from utils.logger import logger


class UserEntity:
    def __init__(self, phone_number, session_name, code=None, is_code_send=False):
        self.phone_number = phone_number
        self.session_name = session_name
        self.code = code
        self.is_code_send = is_code_send


async def get_users_from_db():
    conn = get_connection()
    users = []
    logger.info(f"Start fetching users")
    try:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT phone_number, session_name, code, is_code_send FROM users")
            rows = cur.fetchall()

            for row in rows:
                users.append(UserEntity(
                    phone_number=row['phone_number'],
                    session_name=row['session_name'],
                    code=row['code'],
                    is_code_send=row['is_code_send']
                ))
    except Exception as e:
        logger.error(f"Error fetching users: {e}")
    finally:
        conn.close()

    return users

async def wait_for_code(user):
    conn = get_connection()
    try:
        while not user.code:
            try:
                with conn.cursor(cursor_factory=RealDictCursor) as cur:
                    cur.execute(
                        sql.SQL("SELECT code FROM users WHERE phone_number = %s"),
                        [user.phone_number]
                    )
                    result = cur.fetchone()
                    if result and result['code']:
                        user.code = result['code']
                        logger.info(f"Code for {user.phone_number} retrieved: {user.code}")
                        break
                    else:
                        logger.info(f"No code found yet for {user.phone_number}, retrying in 10 seconds...")

            except Exception as e:
                logger.info(f"Error fetching code for user {user.phone_number}: {e}")

            await asyncio.sleep(10)
    finally:
        conn.close()