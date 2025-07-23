from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

DATABASE_URL = os.environ.get("DATABASE_URL", "postgresql://user:password@db:5432/database")

engines = create_engine(DATABASE_URL)

session = sessionmaker(autocommit=False, autoflush=False, bind=engines)

Base = declarative_base()