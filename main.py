#!/usr/bin/python
print("Content-Type: text/html")
print()

import cgitb
cgitb.enable()

from jinja2 import Template
import pymysql

from config import connectDB

#connect db
config = connectDB()
conn = pymysql.connect(
    db = config["db"],
    user = config["user"],
    passwd = config["passwd"],
    host = config["host"]
    )

c = conn.cursor()
c.execute("SELECT * FROM userinfo")
data = [(row[1], row[2], row[3], row[4]) for row in c.fetchall()]

fhtml = open("index.html",'r').read()
template = Template(fhtml)

print(template.render(
    info = data
    ))