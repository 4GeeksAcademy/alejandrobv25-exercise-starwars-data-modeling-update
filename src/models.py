import os
import sys
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
from sqlalchemy import create_engine, ForeignKey
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(nullable=False, unique=True)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)

    favorites = relationship('UserFavorites', back_populates='user')

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email
        }


class Character(Base):
    __tablename__ = 'character'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description
        }


class Planet(Base):
    __tablename__ = 'planet'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    population: Mapped[int] = mapped_column(nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "population": self.population
        }


class Movie(Base):
    __tablename__ = 'movie'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)
    release_date: Mapped[str] = mapped_column(nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "release_date": self.release_date
        }


class UserFavorites(Base):
    __tablename__ = 'user_favorites'
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'), primary_key=True)
    movie_id: Mapped[int] = mapped_column(ForeignKey('movie.id'), nullable=True)
    character_id: Mapped[int] = mapped_column(ForeignKey('character.id'), nullable=True)
    planet_id: Mapped[int] = mapped_column(ForeignKey('planet.id'), nullable=True)


    user = relationship('User', back_populates='favorites')
    movie = relationship('Movie')
    character = relationship('Character')
    planet = relationship('Planet')

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "movie_id": self.movie_id,
            "character_id": self.character_id,
            "planet_id": self.planet_id
        }

# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
