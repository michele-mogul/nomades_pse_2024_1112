from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import as_declarative, declared_attr

Base = declarative_base()


@as_declarative()
class BaseWithUtilities:
    id: int

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()
