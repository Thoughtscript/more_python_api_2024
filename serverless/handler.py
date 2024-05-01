import json
import psycopg2

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