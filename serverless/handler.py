import json
import psycopg2
import urllib3

def examples(event, context):
    conn = psycopg2.connect(dbname="postgres", user="testuser", password="testpassword", host="postgres", port="5432")

    cur = conn.cursor()
    cur.execute("SELECT * FROM example;")
    record_set = cur.fetchone()

    cur.close()
    conn.close()

    return {"statusCode": 200, "body": json.dumps(record_set)}

def psql_json(event, context):
    conn = psycopg2.connect(dbname="postgres", user="testuser", password="testpassword", host="postgres", port="5432")

    cur = conn.cursor()
    cur.execute("SELECT arr -> 'id' AS json_id, arr -> 'name' AS json_name FROM example e, json_array_elements(e.json_array_col) arr WHERE (arr ->> 'id')::int > -1;")
    record_set = cur.fetchone()

    cur.close()
    conn.close()

    return {"statusCode": 200, "body": json.dumps(record_set)}

def other_api(event, context):
    http = urllib3.PoolManager()
    response = http.request("GET", "http://fastapi:8000/examples", headers={"Content-Type": "application/json"})
    return {"statusCode": 200, "body": str(response.json())} # todo - this could be parsed more elegantly - causes issues with postman but I found a workaround
