from fastapi import APIRouter
import psycopg #psycopg3

examples_api = APIRouter()

# Singleton
conn = psycopg.connect(dbname="postgres", user="testuser", password="testpassword", host="postgres", port="5432")

@examples_api.get("/examples")
async def examples():
    # the following will automatically close the cursor after the block completes
    # https://www.psycopg.org/psycopg3/docs/api/connections.html
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM example;")
        record_set = cur.fetchone()
    
        #cur.close() # will auto close
        #conn.close() # will be kept open
        return record_set