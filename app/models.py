from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import CheckConstraint

from .database import Base


class Tag(Base):
    __tablename__ = 'tag'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20), index=True)

    # many-to-many relation

    places = relationship('Place',
                          secondary='tag_place',
                          back_populates='tags')


class Place(Base):
    __tablename__ = 'place'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    review = Column(Integer, CheckConstraint('0 < review <= 5'))
    city = Column(String)
    site = Column(String)

    # many-to-many relationship

    tags = relationship('Tag',
                        secondary='tag_place',
                        back_populates='places')

    userlists = relationship('UserList',
                             secondary='userlist_place',
                             back_populates='places')


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    # one-to-many relationship

    userlists = relationship('UserList', back_populates='owner')


class UserList(Base):
    __tablename__ = 'userlist'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)

    # many-to-one relationship

    owner_id = Column(Integer, ForeignKey('user.id'))
    owner = relationship('User', back_populates='userlists')

    # many-to-many relationship

    places = relationship('Place',
                          secondary='userlist_place',
                          back_populates='userlists')


# association tables

class TagPlace(Base):
    __tablename__ = 'tag_place'

    tag_id = Column(Integer, ForeignKey('tag.id'), primary_key=True)
    place_id = Column(Integer, ForeignKey('place.id'), primary_key=True)


class UserlistPlace(Base):
    __tablename__ = 'userlist_place'

    place_id = Column(Integer, ForeignKey('place.id'), primary_key=True)
    userlist_id = Column(Integer, ForeignKey('userlist.id'), primary_key=True)
