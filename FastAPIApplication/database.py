from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:test12345!@localhost/QAA"
#                                       { USER } {PASSWORD} { HOST  } {DATABASE}

engine = create_engine(SQLALCHEMY_DATABASE_URL)
# creating a database engine using the url we just created above ^^

session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# making a local session, this is binded to the engine

base = declarative_base()
# creating a base to use for the database in upcoming api calls