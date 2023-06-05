import os

class Config:
    PG_USER = os.getenv('PG_USER')
    PG_PASS = os.getenv('PG_PASS')
    PG_HOST = os.getenv('PG_HOST')
    PG_NAME = os.getenv('PG_NAME')

    DATABASE_URI=f'postgresql+asyncpg://{PG_USER}:{PG_PASS}@{PG_HOST}/{PG_NAME}'
