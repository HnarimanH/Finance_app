import sqlite3
connection = sqlite3.connect("/Users/narimanhosseinzadeh/Documents/Codes/Finance_app/user_purchase.db")
cursor = connection.cursor()

cursor.execute("SELECT user_id, amount, item_action, date FROM user_purchase WHERE user_id == 1")


user_names = cursor.fetchall()
while True:
    try:
        for i, names in enumerate(user_names[0]):
            print(user_names[0][i])
        user_names.remove(user_names[0])
    except IndexError:
        break
    
