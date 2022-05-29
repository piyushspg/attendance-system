import mysql.connector
from flask import Flask, render_template, request, redirect, url_for

# from attendance import Window

print("Content-Type: text/html\n")
conn = mysql.connector.connect(host="localhost", database="sms", user="root")
cursor = conn.cursor()
app = Flask(__name__)


@app.route("/")
def index():
    print('index page')
    return render_template("home.html")


@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/try")
def try1():
    # Window().show_window()
    pass


@app.route("/students")
def students():
    conn.commit()
    sql_query = """
    WITH attendance_cleaned AS (
        SELECT * from attendance GROUP BY name, date
    ), students_with_attendance AS (
        SELECT roll_no, students.name, father_name, class, mobile, email, COUNT(attendance_cleaned.name) as days_present FROM students LEFT JOIN attendance_cleaned ON students.name=attendance_cleaned.name GROUP BY roll_no, students.name, father_name, class, mobile, email
    ), total AS (
        SELECT COUNT(DISTINCT date) as total_days from attendance
    )
    SELECT students_with_attendance.*, (days_present / total_days * 100) as attendance from students_with_attendance cross join total;
    """
    # sql_query = "SELECT * from students;"
    cursor.execute(sql_query)
    value = cursor.fetchall()
    return render_template("index.html", data=value)


if __name__ == "__main__":
    app.run(debug=True)


# SELECT students.*, COUNT(attendance.name) as days_present FROM students LEFT JOIN attendance ON students.name=attendance.name GROUP BY students.name