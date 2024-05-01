from fastapi import FastAPI
import psycopg2

app = FastAPI()

@app.get("/")
async def test():
    return {"message": "Hello World"}

@app.get("/examples")
async def examples():
    conn = psycopg2.connect(dbname="postgres", user="testuser", password="testpassword", host="postgres", port="5432")

    cur = conn.cursor()
    cur.execute("SELECT * FROM example;")
    record_set = cur.fetchone()
    
    cur.close()
    conn.close()
    return record_set