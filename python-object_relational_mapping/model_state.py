#!/usr/bin/python3
"""
defines state class mapped to states table in mysql using sqlalchemy
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class State(Base):
    """state class mapped to states table"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    USER = 'root'
    PASSWORD = 'root'
    DB_NAME = 'hbtn_0e_0_usa'
    engine = create_engine(
        f'mysql+mysqldb://{USER}:{PASSWORD}@localhost:3306/{DB_NAME}',
        pool_pre_ping=True
        )

    Base.metadata.create_all(engine)
