from psycopg2 import sql

import json
import psycopg2

from config import connect

def deleteDataFunc(i_d: int):
    data = []
    try:
        conn = connect()
        cur = conn.cursor()

        cur.execute("""DELETE FROM public.users WHERE id = '{id}' """.format(id = i_d))
        conn.commit()
        result = cur.rowcount
        cur.close()

        if result:
            data.append({"status": 200, "message":"Success", "body": {}})
        else:
            data.append({"status": 404,"message": "No list of users", "body": {}})
        
        return data


    except psycopg2.DatabaseError as error:
        data.append({"status": 500,"message": "Server internal error", "body": {}})
        print("Failed to get list of users, error: ", error)
        return data

