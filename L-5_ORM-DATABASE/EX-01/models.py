from sqlalchemy import Column , Integer , String
from sqlalchemy.ext.declarative import declarative_base # การประกาศตัว database

Base = declarative_base() # สร้าง schema database

class User(Base): # เรียก class User จะมี orbject Base
    __tablename__ = 'users' # ชื่อ table name 'users'
    id = Column(Integer,primary_key=True) # ใน Column จะมี integer และเป็น primary_key ห้ามซ้ำ
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    def __repr__(self):
        return "<User(name='%s',fullname='%s',nickname = '%s')>" % (self.name,self.fullname,self.nickname) # ตัวเริ่มต้น 