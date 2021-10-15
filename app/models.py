from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import CheckConstraint

from .database import Base


class Tag(Base):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20), index=True)

    places = relationship('Place')


class Place(Base):
    __tablename__ = 'places'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    review = Column(Integer, CheckConstraint('0 < review <= 5'))
    city = Column(String)
    site = Column(String)

    tags = relationship('Tag', back_populates='places')


class UserList(Base):
    __tablename__ = 'userlists'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50))
    description = Column(String)
    
    places = relationship('Place')
    owner = relationship('User', back_populates='lists', uselist=False)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    lists = relationship('UserList', back_populates='owner')
