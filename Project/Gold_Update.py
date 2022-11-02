from bs4 import BeautifulSoup
import requests
from sqlalchemy import create_engine
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import CHAR, VARCHAR, Column, Integer, ForeignKey, String
from sqlalchemy.orm import sessionmaker
import time

engine = sqlalchemy.create_engine('postgresql://webadmin:RTTooa27373@node36662-jakapat.proen.app.ruk-com.cloud:5432/login') #11243 Database postgresSQL
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


url = 'https://www.goldtraders.or.th'
req = requests.get(url)
req.encoding = 'utf-8'
sup = BeautifulSoup(req.text,'lxml')

lastup = '29/10/2565 เวลา 09:00 น. (ครั้งที่ 1)'


class goldthaistick(Base):
    __tablename__ = "goldthaistick"
    id = Column(Integer, primary_key=True)
    gold = Column(String,nullable=False)
    time = Column(String, nullable=False)
    sell = Column(String, nullable=False)
    buy = Column(String, nullable=False)

class goldthairoopapan(Base):
    __tablename__ = "goldthairoopapan"
    id = Column(Integer, primary_key=True)
    gold_roop = Column(String,nullable=False)
    time_roop = Column(String, nullable=False)
    sell_roop = Column(String, nullable=False)
    buy_roop = Column(String, nullable=False)

Time_stick = sup.find(id="DetailPlace_uc_goldprices1_lblAsTime")
Sell_stick = sup.find(id="DetailPlace_uc_goldprices1_lblBLSell")
Buy_stick = sup.find(id="DetailPlace_uc_goldprices1_lblBLBuy")

Time_roopapan = sup.find(id="DetailPlace_uc_goldprices1_lblAsTime")
Sell_roopapan = sup.find(id="DetailPlace_uc_goldprices1_lblOMSell")
Buy_roopapan = sup.find(id="DetailPlace_uc_goldprices1_lblOMBuy")

while True:
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    save_goldthai_stick = goldthaistick(gold='ทองแท่ง',time=str(Time_stick.string),sell=str(Sell_stick.string),buy=str(Buy_stick.string))
    save_goldthai_roopapan = goldthairoopapan(gold_roop='ทองรูปพรรณ',time_roop=str(Time_roopapan.string),sell_roop=str(Sell_roopapan.string),buy_roop=str(Buy_roopapan.string))

    session.add(save_goldthai_stick)
    session.add(save_goldthai_roopapan)
    session.commit()

    time.sleep(18000)
