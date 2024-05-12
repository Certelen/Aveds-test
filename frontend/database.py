import sqlalchemy
from settings import SQLALCHEMY_DATABASE_URL

engine = sqlalchemy.create_engine(SQLALCHEMY_DATABASE_URL)
connection = engine.raw_connection()
