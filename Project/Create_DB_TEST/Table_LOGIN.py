import psycopg2
from psycopg2 import Error 

try:
    connection = psycopg2.connect(user='webadmin',
                                    password='RTTooa27373',
                                    host='node36662-jakapat.proen.app.ruk-com.cloud',
                                    port='11243',
                                    database='login')

    cursor = connection.cursor()

    create_table_guery = '''CREATE TABLE accounts
        (id SERIAL PRIMARY KEY,
        username      VARCHAR(50) NOT NULL,
        password      VARCHAR(50) NOT NULL,
        email      VARCHAR(255) NOT NULL,
        tel     INTEGER NOT NULL); '''

    cursor.execute(create_table_guery)
    connection.commit()
    print("Table created successfully in PostgreSOL ")

except (Exception, psycopg2.DatabaseError) as error: 
    print("Error while creating PostgreSQL table", error) 
finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSOL connection is closed")