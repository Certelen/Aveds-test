from dotenv import load_dotenv
from fastapi.security import OAuth2PasswordBearer
import os


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
load_dotenv()

DB_NAME = os.getenv('DB_NAME', 'postgres')
DB_USERNAME = os.getenv('DB_USERNAME', 'postgres')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'postgres')
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = os.getenv('DB_PORT', '5432')
SECRET = os.getenv('SECRET', '')

SQLALCHEMY_DATABASE_URL = ((
    f'postgresql+psycopg2://\
{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
))

NAME_LENGHT = 20
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
