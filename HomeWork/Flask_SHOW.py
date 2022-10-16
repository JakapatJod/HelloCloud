from flask import Flask,render_template,request  # ตอนนี้ run เป็น Local เซิฟ
from flask_sqlalchemy import SQLAlchemy # มาทำเพื่อ DB model ใน columns

app =  Flask(__name__)

@app.route('/')
def index():
    return render_template('ShowTable.html')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
