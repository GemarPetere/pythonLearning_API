from psycopg2 import sql

import json
import psycopg2

from config import connect


def addDataFunc(firstName:str, lastName:str, age:str, gender:str, address:str):
    data = []
    try:
        conn = connect()
        cur = conn.cursor()

        stmt = sql.SQL(""" INSERT INTO public.postgres(first_name, last_name, age, gender, address)
                           SELECT '{firstName}', '{lastName}', '{age}', '{gender}', '{address}'
                           WHERE
                                NOT EXISTS (
                                    SELECT id FROM public.postgres 
                                    WHERE first_name = '{firstName}' AND last_name = '{lastName}'
                                )
                        """.format(firstName = firstName,
                                   lastName = lastName,
                                   age = age,
                                   gender = gender,
                                   address = address))
        cur.execute(stmt)
        conn.commit()
        result = cur.rowcount
        cur.close()

        if result:
            data.append({"status":200, "message":"Added Succesffuly", "body":{}})
        else:
            data.append({"status":406, "message":"Not Acceptable, Data Already Exist!", "body": {}})   
            


    except psycopg2.DatabaseError as error:
        print("Internal Server Error: ",error)
        data.append({"status":500, "message":"Internal Server Error"})
        return data
