import json
from flask_cors import CORS
import psycopg2
from psycopg2 import sql
from flask import Flask, request
from decouple import config

app = Flask(__name__)
CORS(app)

def get_db_connection():
    database= config('DATABASE')
    user = config('USER')
    password = config('PASSWORD')

    conn = psycopg2.connect(host='localhost',
                            database=database,
                            user=user,
                            password=password)
    return conn

@app.route('/create-account', methods=['POST'])
def create_account():
    conn = get_db_connection()
    cur = conn.cursor()
    first_name = 'John'
    last_name = 'Doe'
    request_body = request.get_json()
    email = request_body.get('email')
    password = request_body.get('password')
    profession = request_body.get('professsion')
    cur.execute(
        sql.SQL(
            """
                INSERT INTO handy_user_accounts (first_name, last_name, email, password, profession)
                VALUES ({first_name}, {last_name}, {email}, {password}, {profession});
            """
        ).format(
            first_name=sql.Literal(first_name),
            last_name=sql.Literal(last_name),
            email=sql.Literal(email),
            password=sql.Literal(password),
            profession=sql.Literal(profession),
        )
    )
    conn.commit()
    cur.close()
    conn.close()
    response = app.response_class(
        status=200
    )
    return response
    

@app.route('/login', methods=['POST'])
def login():
    conn = get_db_connection()
    cur = conn.cursor()
    email = request.values.get('email')
    password = request.values.get('password')
    cur.execute(sql.SQL('SELECT first_name, last_name, email, profession FROM handy_user_accounts WHERE email={} AND password={}'.format(email, password)))
    result = cur.fetchone()
    user = {
        "first_name": result[0],
        "last_name": result[1],
        "email": result[2],
        "profession": result[3]
    }
    conn.commit()
    cur.close()
    conn.close()
    return json.dumps(user)


@app.route('/logout')
def logout():
    return json.dumps({"status": '200'})

app.run(host = '0.0.0.0', port = 5000)

