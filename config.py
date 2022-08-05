from decouple import config
import psycopg2

def connect():
    connection = None
    try:
        connection = psycopg2.connect(user = config('DB_USER'),
                                      password = config('DB_PASSWORD'),
                                      host = config('DB_HOST'),
                                      port = config('DB_PORT'),
                                      database = config('DB_Name'))
        
        return connection
    except (Exception, psycopg2.Error) as error:
        print('Error while connecting to Database', error)
        return connection