import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker # สร้าง orm เป็น object
from models import Base , User # ดึง models.py และ Base User เข้ามา

engine = create_engine('sqlite:///user.sqlite3',echo = False) # สร้าง user.sqlite3 เพื่อที่จะเปิดได้เลย echo ถ้าสร้างอะไรผิดปกติแล้ว ไม่ต้องสร้างออกมา

# Base.metadata.drop_all(engine) # ลบ database ตัวออกทั้งหมด ถ้าเปิดก็จะลบตัวเก่าออกและ ตัว create ก็จะสร้างใหม่
Base.metadata.create_all(engine) # สร้าง database

Session = sessionmaker(bind=engine)
session = Session()

user1 = User(name='user1', fullname='Ed Jones', nickname='ed') # ตัว record ตัวที่ 1

session.add(user1) # สร้างข้อมูลแบบรายบุคคล
session.commit() # บันทึกทันที