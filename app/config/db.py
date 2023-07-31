from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine("sqlite:///ms_user.db", echo=True)
Base = declarative_base()


def start_db():
    Base.metadata.create_all(bind=engine)


Session = sessionmaker(bind=engine)
session = Session()


def save(model):
    session.add(model)
    commit()
    return model


def commit():
    session.commit()
