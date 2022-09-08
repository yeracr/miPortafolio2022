import sqlite3

query = 'select * from comentario'
mycursor = sqlite3.connect('./sanagustin.db')


datos = mycursor.execute(query)

dato = datos.fetchall()
print(dato)