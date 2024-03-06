import os
import sqlite3

import mysql.connector
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

from helpers import apology, login_required

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# MYSQL database connect
db = mysql.connector.connect(host='192.168.3.154', user='root', passwd='1234', database='mydb')
cursor = db.cursor(dictionary=True)

#db 데이터 가져오기
# cursor.fetchall() #모든 행 가져오기
# cursor.fetchone() # 하나의 행만 가져오기
# cursor.fetchmany() # n개의 데이터 가져오기 

# 수정 사항 db에 저장
# db.commit()
 
# Database 닫기
# db.close()



@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/index", methods=["GET", "POST"])
def index_():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        
        # Ensure username was submitted
        if not request.form.get("user_email"):
            print("빠가야로")

        # Ensure password was submitted
        elif not request.form.get("user_pwd"):
            print("도라이")

        # Query database for username
        cursor.execute(f"SELECT * FROM user WHERE user_email = '{request.form.get("user_email")}'")
        rows_email = cursor.fetchall()
        
        cursor.execute(f"SELECT * FROM user WHERE user_pwd = '{request.form.get("user_pwd")}'")
        rows_pwd = cursor.fetchall()
        
        

        # Ensure username exists and password is correct
        if rows_email and rows_pwd:
            print("바보천지")

        # Remember which user has logged in
        session["user_email"] = rows_email[0]["user_email"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("index.html")

@app.route("/month", methods=["GET", "POST"])
def month():
    if request.method == "POST":
        return render_template("month.html")
    else:
        return render_template("month.html")

@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route("/signup", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        user_email = request.form.get("user_email")
        user_pwd = request.form.get("user_pwd")
        try:
            cursor.execute(f"INSERT INTO user user_email, user_pwd = '{request.form.get("user_email")}', '{request.form.get("user_email")}'")
        except:
            print("ERROR")
        
    # GET 요청인 경우에는 register.html을 렌더링합니다.
    return render_template("signup.html")

@app.route("/user")
def user():
    user = db.execute("SELECT * FROM user")
    return render_template("index.html", user=user)

@app.route("/board", methods=["GET", "POST"])
@login_required
def board():
    if request.method == "POST":
        board_title = request.form.get("board_title")
        board_content = request.form.get("board_content")
        board_date = request.form.get("board_date")
        if board_title is None:
            return apology()
        elif board_content is None:
            return apology()
        elif board_content is None:
            return apology()
        board_write = db.execute("INSERT INTO board (board_title, board_content, board_date, user_email) VALUES(?, ?, ?, ?)", board_title, board_content, board_date, user_email)
    else:
        return render_template("board.html")
    