#!/usr/bin/python3
"""
prints all city objects from DB
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]


    engine = create_engine(
        f"mysql+mysqldb://{user}:{passwd}@localhost:3306/{db_name}",
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()


    search = session.query(City, State).join(State).order_by(City.id).all()

    for city, state in search:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.commit()
    session.close()
