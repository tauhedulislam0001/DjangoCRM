#  For create database you can use this command

import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'nrb123456',
)


# prepare cursor object
cursorObject = database.cursor()


# create database
cursorObject.execute("CREATE DATABASE elderco")

print("ALL DONE!")