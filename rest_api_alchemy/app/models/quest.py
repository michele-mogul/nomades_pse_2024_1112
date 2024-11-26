from sqlalchemy import Column, Integer, String

from app.db.base import Base


class Quest(Base):
    __tablename__ = "quests"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    description = Column(String(200))
