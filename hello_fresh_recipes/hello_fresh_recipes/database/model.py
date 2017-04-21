from sqlalchemy import create_engine, Column, ForeignKey, Integer, String
from sqlalchemy import Numeric, DateTime, Binary, Enum, func
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Asset(Base):
    __tablename__ = 'assets'
    id = Column(Integer, primary_key=True)
    recipe_id = Column(Integer, ForeignKey('recipes.id'))
    type = Column(Enum('image', 'thumbnail', 'pdf'))
    url = Column(String)
    size = Column(Numeric)
    size_unit = Column(String)
    path = Column(String)
    filename = Column(String)
    downloaded = Column(Binary)
    download_date = Column(DateTime)


class Recipe(Base):
    __tablename__ = 'recipes'
    id = Column(Integer, primary_key=True)
    uid = Column(String, nullable=False, unique=True)
    country = Column(String)
    name = Column(String)
    headline = Column(String)
    difficulty = Column(Integer)
    favorites = Column(Integer)
    rating = Column(Numeric)
    slug = Column(String)
    description = Column(String)
    url = Column(String)
    published_date = Column(DateTime)
    created_date = Column(DateTime, default=func.now())
    assets = relationship(Asset, backref='recipes')
