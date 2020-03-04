import pyodbc # pip install pyodbc
conn = pyodbc.connect('Server=localhost;Database=Library;Trusted_Connection=Yes;Driver={SQL Server};')

cursor = conn.cursor()
cursor.execute('SELECT * FROM students')

for row in cursor:
    print(row[0] + ' ' + row[1])