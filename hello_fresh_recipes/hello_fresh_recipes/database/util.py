from os import path

from engine import engine, DB_FILE
from model import Base


def init():
    if not path.exists(DB_FILE):
        print 'creating database and schema (%s)' % DB_FILE
        Base.metadata.create_all(engine)

if __name__ == '__main__':
    init()
