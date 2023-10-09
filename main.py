import mysql.connector

connection = mysql.connector.connect(
    user='root',
    password='', # Change to your password
    host='localhost',
    database='python',
    auth_plugin='mysql_native_password')

insertQuery = "INSERT INTO users(username, city) VALUES(%(username)s, %(city)s)"
insertData = {
    'username' : 'Mariusz',
    'city': 'Warszawa'
}

cursor = connection.cursor()
cursor.execute(insertQuery, insertData)

connection.commit()

query = 'SELECT id, username, city FROM users'

cursor.execute(query)

for (id, username, city) in cursor:
    print(f'{id} - {username} from {city}')