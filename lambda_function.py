import os
import pymysql

# env
HOST = os.environ['HOST']
USER = os.environ['USER']
PASSWORD = os.environ['PASSWORD']
DB = os.environ['DB']

print("1>>>>>>>>>>>>>>>>>>>>>>>>>>")
print(HOST)

connection = pymysql.connect(
    host=HOST,
    user=USER,
    password=PASSWORD,
    database=DB,
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor)
print("2>>>>>>>>>>>>>>>>>>>>>>>>>>")
cursor = connection.cursor()

print("3>>>>>>>>>>>>>>>>>>>>>>>>>>")

def lambda_handler(event, context):
    print("3>>>>>>>>>>>>>>>>>>>>>>>>>>")
    users = []
    with connection.cursor() as cursor:
        print("4>>>>>>>>>>>>>>>>>>>>>>>>>>")
        sql = f'''
            SELECT
                *
            FROM
                users
            '''
        cursor.execute(sql)
        users = cursor.fetchall()
    print("5>>>>>>>>>>>>>>>>>>>>>>>>>>")
    return {'users': users}