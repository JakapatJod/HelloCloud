from sqlalchemy import Column , Integer , String , Text , DateTime ,Float ,Boolean ,PickleType
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Member(Base):
    __tablename__ = 'member' # Tablename member
    id = Column(Integer,primary_key = True ,nullable = False) # nullable ห้ามว่าง
    name = Column(String(100), nullable = False)
    description = Column(Text, nullable = True) # nullable ไม่ใส่ก็ได้
    join_date = Column(DateTime, nullable = False)
    vip = Column(Boolean , nullable = False)
    number = Column(Float , nullable =False)

    def __repr__(self):
        return '<UserModel model {}>'.format(self.id)