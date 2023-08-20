import os
import pymysql

# env
HOST = os.environ['HOST']
USER = os.environ['USER']
PASSWORD = os.environ['PASSWORD']
DB = os.environ['DB']

print(HOST)
print(USER)
print(PASSWORD)
print(DB)

connection = pymysql.connect(
    host=HOST,
    user=USER,
    password=PASSWORD,
    database=DB
)

cursor = connection.cursor()

def lambda_handler(event, context):
    users = []
    with connection.cursor() as cursor:
        sql = f'''
            SELECT
                *
            FROM
                users
            '''
        cursor.execute(sql)
        users = cursor.fetchall()
    return {'users': users}