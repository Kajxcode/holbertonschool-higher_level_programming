#!/usr/bin/python3
"""
defines a city class mapped to cities table in mysql using alchemy
"""

from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class City(Base):
    """city class mapped to cities table"""
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)


if __name__ == "__main__":
    USER = 'root'
    PASSWORD = 'root'
    DB_NAME = 'hbtn_0e_0_usa'
    engine = create_engine(
        f'mysql+mysqldb://{USER}:{PASSWORD}@localhost:3306/{DB_NAME}',
        pool_pre_ping=True
        )

    Base.metadata.create_all(engine)
