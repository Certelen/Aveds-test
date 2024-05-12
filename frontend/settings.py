import os

from dotenv import load_dotenv

load_dotenv()

TG_TOKEN = os.getenv('TG_TOKEN', '')
DB_NAME = os.getenv('DB_NAME', 'postgres')
DB_USERNAME = os.getenv('DB_USERNAME', 'postgres')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'postgres')
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = os.getenv('DB_PORT', '5432')
SECRET = os.getenv('SECRET', '')
HOST = os.getenv('HOST', 'http://127.0.0.1:8000/')

SQLALCHEMY_DATABASE_URL = ((
    f'postgresql+psycopg2://\
{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
))
