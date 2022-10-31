from bs4 import BeautifulSoup
import requests
from sqlalchemy import create_engine
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import CHAR, VARCHAR, Column, Integer, ForeignKey, String
from sqlalchemy.orm import sessionmaker
import time
import psycopg2

engine = sqlalchemy.create_engine('postgresql://webadmin:RTTooa27373@node36662-jakapat.proen.app.ruk-com.cloud:11243/project') #11243 Database postgresSQL
Base = declarative_base()


url = 'https://www.goldtraders.or.th'
req = requests.get(url)
req.encoding = 'utf-8'
sup = BeautifulSoup(req.text,'lxml')

lastup = '29/10/2565 เวลา 09:00 น. (ครั้งที่ 1)'

#def GoldpriceCheck():
 #   print("ราคาทองตามประกาศของสมาคมค้าทองคำ")
  #  print('ประจำวันที่ ' + sup.find(id="DetailPlace_uc_goldprices1_lblAsTime").text)
   # print('ทองคำแท่ง 96.5%')
    #print('ขายออก '+ sup.find(id="DetailPlace_uc_goldprices1_lblBLSell").text + ' บาท')
    #print('รับซื้อ '+ sup.find(id="DetailPlace_uc_goldprices1_lblBLBuy").text + ' บาท')
    #print('ทองรูปพรรณ 96.5%')
    #print('ขายออก '+ sup.find(id="DetailPlace_uc_goldprices1_lblOMSell").text + ' บาท')
    #print('ฐานภาษี '+ sup.find(id="DetailPlace_uc_goldprices1_lblOMBuy").text + ' บาท')

class Data_table(Base):
    __tablename__ = "GoldpriceCheck"
    id = Column(Integer, primary_key=True)
    subject_id = Column(String, nullable=False)


Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

Time = sup.find(id="DetailPlace_uc_goldprices1_lblAsTime")
Sell = sup.find(id="DetailPlace_uc_goldprices1_lblBLSell")
Buy = sup.find(id="DetailPlace_uc_goldprices1_lblBLBuy")

while True:

    if lastup != Time:
        print('วัน',Time.string)
        print('ขายออก',Sell.string)
        print('ซื้อ',Buy.string)
    time.sleep(5)
    connection = psycopg2.connect(user='webadmin',
                                    password='RTTooa27373',
                                    host='node36662-jakapat.proen.app.ruk-com.cloud',
                                    port='5432',
                                    database='project')        
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM test')
    money_records = cursor.fetchall()
    postgres_insert_query = """ INSERT INTO test (time , sell, buy) VALUES (%s,%s,%s)"""

    rec = str(Time.string),str(Sell.string),str(Buy.string)

    cursor.execute(postgres_insert_query,rec)
    #money_records = cursor.fetchall()

    connection.commit()
    #print(money_records)