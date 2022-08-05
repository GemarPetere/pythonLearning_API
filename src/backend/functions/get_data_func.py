from psycopg2 import sql

import json
import psycopg2

from config import connect

def getDataFunc(i_d: int):
    data = []
    tempdata = []
    try:
        conn = connect()
        cur = conn.cursor()

        cur.execute("""SELECT * FROM public.postgres WHERE id = '{id}' """.format(id = i_d))
        conn.commit()
        user = cur.fetchall()
        result = cur.rowcount
        cur.close()

        if result:
            for row in user:
                tempdata.append({"firstname":row[0],
                                 "lastname":row[1],
                                 "age":row[2],
                                 "gender":row[3],
                                 "address":row[4],})
            
            data.append("status": 200, "message":"Success", "body": tempdata)
        else:
            data.append({"status": 404,"message": "No list of users", "body": {}})
        
        return data


    except psycopg2.DatabaseError as error:
        data.append({"status": 500,"message": "Server internal error", "body": {}})
        print("Failed to get list of users, error: ", error)
        return data

