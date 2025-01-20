import sqlite3
connection = sqlite3.connect("/Users/narimanhosseinzadeh/Documents/Codes/Finance_app/user_purchase.db")
cursor = connection.cursor()

cursor.execute("SELECT user_id, amount, item_action, date FROM user_purchase")


user_names = cursor.fetchall()

print(user_names)