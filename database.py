import sqlite3

def createdb():
    con = sqlite3.connect("data.db")
    cursor = con.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS data(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                content TEXT,
                author TEXT
            )          
        ''')
    con.commit()
    cursor.close()
    con.close()

def storedb(title,content,author):
    con = sqlite3.connect("data.db")
    cursor = con.cursor()
    cursor.execute('''
            INSERT INTO data (title, content, author)
            VALUES (?, ?, ?)
        ''', (title, content, author))
    con.commit()