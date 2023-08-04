import sqlite3


def connection(db):
    con = None
    try:
        con = sqlite3.connect(db)
    except Error as e:
        print(f"Error while connecting to the DB: {e}")
    return con


def insert(con, table, data):
    if table == "imb_pingpong":
        query = f"""INSERT INTO {table}(jobid,date,byte,mb_per_sec) VALUES(?,?,?,?)"""
    if table == "imb_bidir_get":
        query = f"""INSERT INTO {table}(jobid,date,byte,mb_per_sec,mode) VALUES(?,?,?,?,?)"""

    # cur = con.cursor()
    try:
        cur = con.cursor()
        cur.execute(query, data)
        con.commit()
        print("success")
        return "success"
    except Exception as e:
        print(f"{e}")
        return f"Error: {e}"
