import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, session, redirect, url_for, render_template, flash , request
from sqlalchemy import Column , Integer , String , ForeignKey
from Gold_Update import goldthairoopapan , goldthaistick ,session


import psycopg2  
import psycopg2.extras


app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://webadmin:RTTooa27373@10.104.4.188:5432/login'
#app.config['SQLALCHEMY_DATABASE_URI']='postgresql://webadmin:RTTooa27373@node36662-jakapat.proen.app.ruk-com.cloud:11243/login' # define ของ databaseSQL ดึง database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # ปิดข้อความโชว์ ถ้าจะเปิดให้เป็น True
app.config['SQLALCHEMY_KEY'] = 'how_to_Get_KEY' 


@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/login',methods=["GET","POST"])
def login():
    if request.method=='POST':
        username = request.form['username']
        password = request.form['password']
        connection = psycopg2.connect(user='webadmin',
                                    password='RTTooa27373',
                                    host='node36662-jakapat.proen.app.ruk-com.cloud',
                                    port='5432',
                                    database='login')

        # connection.row_factory = psycopg2.Row

        cursor = connection.cursor()
        postgresSQL_select_Query = "select * from accounts where username = %s and password = %s "
        record_to_select = (username,password)


        cursor.execute(postgresSQL_select_Query,record_to_select)
        data = cursor.fetchone()

        if data:
            # session["username"] = data["username"]
            # session["password"] = data["password"]
            return redirect("customer")
        else:
            flash("Username and Password Mismatch","danger")
    return redirect(url_for("index"))

@app.route('/customer',methods=["GET","POST"])
def customer():
    return render_template("customer.html")

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method=='POST':
        try:
            username = request.form['username']
            passwords = request.form['passwords']
            email = request.form['email']
            contact = request.form['contact']
            connection = psycopg2.connect(user='webadmin',
                                    password='RTTooa27373',
                                    host='node36662-jakapat.proen.app.ruk-com.cloud',
                                    port='5432',
                                    database='login')
            cursor = connection.cursor()
    
            postgres_insert_query = """ INSERT INTO accounts (username, password , email , tel) VALUES (%s,%s,%s,%s)"""
            record_to_insert = (username,passwords,email,contact)
            cursor.execute(postgres_insert_query,record_to_insert)
            connection.commit()
            flash("Record Added  Successfully","success")

        except:
            flash("Error in Insert Operation","danger")

        finally:
            if connection:
                cursor.close()
                connection.close()
            return redirect(url_for("index"))
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for("index"))

@app.route('/check')
def check():
    Data = session.query(goldthaistick.time,goldthaistick.sell)
    return render_template('check.html')

@app.route('/team')
def team():
    return render_template('team.html')

if __name__ == '__main__':
    app.secret_key = 'how_to_Get_KEY'
    app.run(debug=True,port=80,host='0.0.0.0')
