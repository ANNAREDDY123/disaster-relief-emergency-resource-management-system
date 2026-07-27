from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String

from database import Base


class Volunteer(Base):

    __tablename__ = "volunteers"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable=False)

    email = Column(String(100), unique=True, nullable=False)

    phone = Column(String(15), nullable=False)

    assigned_camp = Column(
        Integer,
        ForeignKey("camps.id"),
        nullable=True
    )

    availability_status = Column(
        Boolean,
        default=True
    )
