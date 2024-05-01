from fastapi import APIRouter
import psycopg2

examples_api = APIRouter()

@examples_api.get("/examples")
async def examples():
    conn = psycopg2.connect(dbname="postgres", user="testuser", password="testpassword", host="postgres", port="5432")

    cur = conn.cursor()
    cur.execute("SELECT * FROM example;")
    record_set = cur.fetchone()
    
    cur.close()
    conn.close()
    return record_set