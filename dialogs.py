import sqlite3


def read_dialogs():
    connection = sqlite3.connect("dialogs.db")
    cursor = connection.cursor()
    cursor.execute("SELECT text FROM Dialog")
    tmp = cursor.fetchall()
    result = []
    for i in range(len(tmp)):
        result.append(tmp[i][0])
    connection.close()
    return result
