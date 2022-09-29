from flask import Flask,render_template,request,redirect,url_for  # ตอนนี้ run เป็น Local เซิฟ
from flask_sqlalchemy import SQLAlchemy # มาทำเพื่อ DB model ใน columns
from sqlalchemy import Column,Integer,String,Date # ประเภทของ columns มีอะไรบ้าง

app =  Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://webadmin:RTTooa27373@10.104.4.188:5432/testdb' # define ของ databaseSQL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # ปิดข้อความโชว์ ถ้าจะเปิดให้เป็น True

db = SQLAlchemy(app)

class Comments(db.Model): 
    __tablename__ = 'comments' # เรียกใช้ table ที่ชื่อว่า comments
    id = Column(Integer,primary_key=True) # primary_key คือซ้ำไม่ได้
    name = Column(String)
    comment = Column(String)

@app.route('/')
def index():
    result = Comments.query.all() # methods กับ object all
    return render_template('index7.html',result=result) # resulut คือ ข้อมูลที่ดึงออกมาทั้งหมด

@app.route('/sign')
def sign():
    return render_template('sign7.html')

@app.route('/process',methods=['POST'])
def process():  # process ฟอร์มที่รับมาจาก sign
    name = request.form['name']
    comment = request.form['comment']
    signature = Comments(name=name,comment=comment)
    db.session.add(signature)   # signatue จะถูก add เข้าไปใน database
    db.session.commit()
    return redirect(url_for('index'))   # พอทำเสร็จก็จะกลับไปหน้า index

if __name__ == '__main__':
    app.run(debug=True)
# ORM = Online Reputation Management
# WEB --> WEB SERVER -WSGI-> applicating instance --> ORM --> database(postgresSQL)