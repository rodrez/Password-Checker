import sqlite3

conn = sqlite3.connect('PasswordManager.db')

print("Opened database successfully!")

# conn.execute('''CREATE TABLE PASSWORDS
#          (ID INT PRIMARY KEY     NOT NULL,
#          NAME           TEXT    NOT NULL,
#          LOGIN          TEXT    NOT NULL,
#          PASSWORD       TEXT     NOT NULL);''')
# print("Table created successfully");
conn.execute("INSERT INTO PASSWORDS (ID,NAME,LOGIN,PASSWORD) \
      VALUES (2, 'gmail', 'fabian.rodrez@gmail.com', '@Monarch6419' )");
conn.commit()
cursor = conn.execute("SELECT id, name, login, password from PASSWORDS")
for row in cursor:
    print("ID", row[0])
    print("NAME", row[1])
    print("LOGIN", row[2])
    print("PASSWORD", row[3])
    

conn.close()