#!/usr/bin/env python
import os
from os import path
import sqlalchemy
from sqlalchemy import create_engine, Column, ForeignKey, Integer, String, Numeric, DateTime, Binary, Enum, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

try:
    import sqlite3
except ImportError:
    import sqlite as sqlite3

DB_FILE = path.join(os.getcwd(), "database.db")

Base = declarative_base()
Session = sessionmaker()

class db:
    def __init__(self):
        self.engine = None
        self.engine = create_engine('sqlite:///' + DB_FILE, echo=True)
        Session.configure(bind=self.engine)

        if not path.exists(DB_FILE):
            print('creating database and schema (%s)' % DB_FILE)
            Base.metadata.create_all(self.engine)
    
    def add(self, object):
        session = Session()
        session.add(object)
        session.commit()

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


class Recipe(Base):
    __tablename__ = 'recipes'
    id = Column(Integer, primary_key=True)
    uid = Column(String, nullable=False)
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
    downloaded = Column(Binary)
    download_date = Column(DateTime)
    assets = relationship(Asset, backref='recipes')
