from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from database import Base


class Camp(Base):

    __tablename__ = "camps"

    id = Column(Integer, primary_key=True, index=True)

    camp_name = Column(String(100), nullable=False)

    location = Column(String(150), nullable=False)

    district = Column(String(100), nullable=False)

    capacity = Column(Integer, nullable=False)

    available_capacity = Column(Integer, nullable=False)

    status = Column(String(20), nullable=False)
