import sqlite3

conn=sqlite3.connect("emaildb.sqlite")
db=conn.cursor()

db.execute("DROP TABLE IF EXISTS Counts")
db.execute("CREATE TABLE Counts ('org' TEXT, 'count' INTEGER)")
info=db.execute("SELECT * FROM Counts")

file=open("sample.txt")
for line in file:
    if not line.startswith("From "):
        continue

    info=line.split()

    email=info[1]
    lt=email.split("@")
    org=lt[1]

    db.execute("SELECT * FROM Counts WHERE org= ?", (org,))

    row=db.fetchone()

    if row is None:
        db.execute("INSERT INTO Counts (org, count) VALUES(?, 1)", (org,))

    else:
        db.execute("UPDATE Counts SET count=count + 1 WHERE org=?",(org,))

conn.commit()
db.close()
