import psycopg2

def get_connection():
    return psycopg2.connect(
        host='localhost',
        user='postgres',
        password='1234',
        database='ia_universidad'
    )