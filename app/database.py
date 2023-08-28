from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker 

SQLALCHEMY_BASE_URL = 'postgresql://admin:password@localhost:5432/gameperfdb'

engine = create_engine(SQLALCHEMY_BASE_URL)

sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


