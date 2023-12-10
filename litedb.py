import sqlite3,traceback,requests,json

def get_conn(name):
    conn=sqlite3.connect(f"dbs/{name}",check_same_thread=False)
    cursor=conn.cursor()
    query1="CREATE TABLE IF NOT EXISTS main(x TEXT PRIMARY KEY,y TEXT)"
    cursor.execute(query1)
    conn.commit()
    return conn

maps=get_conn("maps.db")

def __set(conn,key,val,iterations=0):
    try:
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM main WHERE x = ?",(key,))
        if len(cursor.fetchall())==0:
            query2="INSERT INTO main VALUES (?,?)"
            cursor.execute(query2,(key,val))
            conn.commit()
        else:
            cursor.execute("UPDATE main SET y = ? WHERE x = ?",(val,key))
            conn.commit()
    except Exception as e:
        if iterations>4:
            traceback.print_exc()
            raise e
        __set(conn,key,val,iterations+1)

def __get(conn,key,iterations=0):
    try:
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM main WHERE x = ?",(key,))
        data=cursor.fetchall()
        if len(data)==0:
            return False
        return list(data[0])[1]
    except Exception as e:
        if iterations>4:
            traceback.print_exc()
            raise e
        return __get(conn,key,iterations+1)

def set(key,val):
    __set(maps,key,requests.get("http://localhost:4000/?data="+f"__db_data__({key})"+json.dumps(val)).text)

def get(key):
    return json.loads(requests.get("https://gateway.lighthouse.storage/ipfs/"+__get(maps,key)).text[len(f"__db_data__({key})"):])