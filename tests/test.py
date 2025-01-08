import sqlite3
connection = sqlite3.connect("/Users/narimanhosseinzadeh/Documents/Codes/Finance_app/user_data.db")
cursor = connection.cursor()

cursor.execute("SELECT user_name, password FROM user_data")


user_names = cursor.fetchall()

print(user_names)