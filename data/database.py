from sqlalchemy import Column, Integer, Float, Date, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


# here is our SQLAlchemy database which contains test center location data
class CovidDb(Base):
    __tablename__ = 'test-centers'
    __table_args__ = {'sqlite_autoincrement': True}
    health_center_name = Column(String)
    operated_by = Column(String)
    street_address = Column(String)
    city = Column(String)
    state = Column(String)
    zip_code = Column(String)
    telephone = Column(String)
    
