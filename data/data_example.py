import pandas

from sqlalchemy import Column, Integer, Float, Date, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


# here is our SQLAlchemy database which contains test center location data
class TestingLocation(Base):
    __tablename__ = 'testing-locations'
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer, primary_key=True, nullable=False)
    health_center_name = Column(String)
    operated_by = Column(String)
    street_address = Column(String)
    city = Column(String)
    state = Column(String)
    zip_code = Column(String)
    telephone = Column(String)


def create_database(file):
    engine = create_engine('sqlite:///covid.db')
    Base.metadata.create_all(engine)

    df = pandas.read_csv(file)
    df.to_sql(con=engine, index_label='id', name=TestingLocation.__tablename__, if_exists='replace')

    session = sessionmaker()
    session.configure(bind=engine)
