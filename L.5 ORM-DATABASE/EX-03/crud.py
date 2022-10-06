### crud.py ###
from datetime import datetime
from contextlib import contextmanager
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import yaml
from configs import DATABASE_URI,f_yam
from models import Base , Book

engine = create_engine(DATABASE_URI)

Session = sessionmaker(bind = engine)

@contextmanager
def session_scope():
    session = Session()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        print('Error')
        raise
    finally:
        session.close()

def recreate_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

def load_yaml(fn):
    with session_scope() as s:
        for data in yaml.load_all(open(fn), Loader=yaml.FullLoader): #โหลด โดยเอาตัวอะไรบ้าง
            bookyml = Book(**data)
            s.add(bookyml)

if __name__ == '__main__':
    recreate_database()
    # add_data()

    book = Book(
        title = 'Deep Learning',
        author = 'Ian Goodfellow',
        pages= 775,
        published = datetime(2016, 11, 18),
        price = 1500
    )
    with session_scope() as s:
        s.add(book)
    load_yaml('books.yaml')