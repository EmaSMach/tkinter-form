from sqlalchemy import Column, String, Integer
from db import Base, engine, Session

from utils import is_viable_string


class Client(Base):
    __tablename__ = 'clients'

    id = Column(Integer, autoincrement=True, primary_key=True)

    name = Column(String)
    surname = Column(String)
    address = Column(String, nullable=True)
    phone = Column(String, nullable=True)

    def __str__(self):
        return f"Cliente {self.surname}, {self.name}"

    def is_valid(self):
        # validating
        if is_viable_string(self.name) and \
            is_viable_string(self.surname) and \
            (is_viable_string(self.address) or self.address is None) and \
            (is_viable_string(self.phone) or self.phone is None):
            return True
        else:
            return False


Base.metadata.create_all(engine)
