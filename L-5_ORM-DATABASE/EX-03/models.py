from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column , Integer ,String , DateTime , Float

Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer , primary_key=True)
    title = Column(String)
    author = Column(String)
    pages = Column(Integer)
    published = Column(DateTime)
    price = Column(Float)

    def __repr__(self) -> str:
        return "<Book(title='{}' , author='{}',pages={}, published ={} , price= {})>" \
            .format(self.title, self.author, self.pages , self.published, self.price)