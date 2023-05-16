import psycopg2

def connectPg():
    conn = psycopg2.connect("dbname=social user=postgres password=admin")
    cur = conn.cursor()

    return cur

    
