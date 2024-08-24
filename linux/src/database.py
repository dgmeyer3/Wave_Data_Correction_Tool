from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

POSTGRES_USERNAME = os.getenv("POSTGRES_USERNAME", "postgres")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "password")
POSTGRES_HOST = os.getenv("POSTGRES_HOST, "localhost")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")
POSTGRES_DB = os.getenv("POSTGRES_DB", "wavedb")

# Construct the database URL
DATABASE_URL = f"postgresql+psycopg2://{POSTGRES_USERNAME}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"


class Database:
    _session_factory = None
    _declarative_base = None

    @classmethod
    def create_session(cls):
        if cls._session_factory is None:
            engine = create_engine(DATABASE_URL, echo=True)
            cls._session_factory = sessionmaker(bind=engine)
        session = cls._session_factory()
        yield session
        session.close()

    @classmethod
    def get_base(cls):
        if cls._declarative_base is None:
            cls._declarative_base = declarative_base()
        return cls._declarative_base
