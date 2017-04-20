#!/usr/bin/env python
import os
from os import path

try:                import sqlite3
except ImportError: import sqlite as sqlite3

DB_FILE = path.join(os.getcwd(), "database.db")
DB_SCHEMA = path.join(os.getcwd(), "src/resources/database_schema.sql")

class db:
    def __init__(self):
        initDb = False
        if path.exists(DB_FILE):
            print('using database file: %s' % DB_FILE)
        else:
            print('database file (%s) not found, creating...')
            initDb = True
        
        self.conn = None
        self.conn = sqlite3.connect(DB_FILE)

        if initDb:
            
