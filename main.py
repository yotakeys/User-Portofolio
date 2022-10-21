#!/usr/bin/python
print("Content-Type: text/html")
print()

import cgitb
cgitb.enable()

from jinja2 import Template
import pymysql

from config import connectDB

if __name__ == "__main__":

    #connect db
    config = connectDB()
    try:
        conn = pymysql.connect(
            db = config["db"],
            user = config["user"],
            passwd = config["passwd"],
            host = config["host"]
            )
    except Exception:
        print("DATABASE CONNECTION ERROR")
        exit()
        

    c = conn.cursor()
    c.execute("SELECT * FROM userinfo")
    datalis = [(row[1], row[2], row[3], row[4], row[5]) for row in c.fetchall()]
    datadic = []
    for row in datalis:
        temp = {
            "nama" : row[0],
            "nrp" : row[1],
            "info" : row[2],
            "img" : row[3],
            "jurusan" : row[4],
        }
        datadic.append(temp)

    fhtml = open("index.html",'r').read()
    template = Template(fhtml)

    print(template.render(
        info = datadic,
        leng = len(datadic)
        ))