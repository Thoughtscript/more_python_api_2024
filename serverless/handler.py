import json
import psycopg #psycopg3
import urllib3

# Singleton
conn = psycopg.connect(dbname="postgres", user="testuser", password="testpassword", host="postgres", port="5432")

def examples(event, context):
    # the following will automatically close the cursor after the block completes
    # https://www.psycopg.org/psycopg3/docs/api/connections.html
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM example;")
        record_set = cur.fetchone()

        #cur.close() # will auto close
        #conn.close() # will be kept open
        return {"statusCode": 200, "body": json.dumps(record_set)}

def psql_json(event, context):
    # the following will automatically close the cursor after the block completes
    # https://www.psycopg.org/psycopg3/docs/api/connections.html
    with conn.cursor() as cur:
        cur.execute("SELECT arr -> 'id' AS json_id, arr -> 'name' AS json_name FROM example e, json_array_elements(e.json_array_col) arr WHERE (arr ->> 'id')::int > -1;")
        record_set = cur.fetchone()

        #cur.close() # will auto close
        #conn.close() # will be kept open
        return {"statusCode": 200, "body": json.dumps(record_set)}

def other_api(event, context):
    http = urllib3.PoolManager()
    response = http.request("GET", "http://fastapi:8000/examples", headers={"Content-Type": "application/json"})
    return {"statusCode": 200, "body": str(response.json())} # todo - this could be parsed more elegantly - causes issues with postman but I found a workaround
