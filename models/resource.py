from sqlalchemy import Column
from sqlalchemy import Date
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String

from database import Base


class Resource(Base):

    __tablename__ = "resources"

    id = Column(Integer, primary_key=True, index=True)

    camp_id = Column(
        Integer,
        ForeignKey("camps.id"),
        nullable=False
    )

    resource_type = Column(String(100), nullable=False)

    quantity = Column(Integer, nullable=False)

    distributed_by = Column(String(100), nullable=False)

    distribution_date = Column(Date, nullable=False)
