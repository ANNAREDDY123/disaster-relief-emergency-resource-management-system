from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String

from database import Base


class Victim(Base):

    __tablename__ = "victims"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable=False)

    age = Column(Integer, nullable=False)

    gender = Column(String(20), nullable=False)

    contact_number = Column(String(15), nullable=False)

    family_members = Column(Integer, nullable=False)

    camp_id = Column(
        Integer,
        ForeignKey("camps.id"),
        nullable=False
    )
