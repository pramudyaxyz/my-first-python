import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = ""
)

if db.is_connected():
    print("Connecting database is work")