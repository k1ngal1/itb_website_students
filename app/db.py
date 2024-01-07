import pymysql

# Connect SQL server


def obtain_connection():
    return pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                port=3307,
                                db='students')
