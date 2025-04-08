import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    DATABASE_URL = os.getenv("DATABASE_URL")
    JWT_SECRET = os.getenv("JWT_SECRET")
    JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")
    JWT_EXPIRATION_TIME = os.getenv("JWT_EXPIRATION_TIME")
    CORS_ORIGINS = os.getenv("CORS_ORIGINS").split(",")


config = Config()
