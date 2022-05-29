import mysql.connector
from flask import Flask, render_template , request ,redirect , url_for

import AttendanceProject from capture1

conn = mysql.connector.connect(host="localhost", database="sms", user="root")

cursor = conn.cursor()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/home")
def capture1():
    return render_template('home.html')

if __name__ == "__main__":
    try1.run(debug=True)