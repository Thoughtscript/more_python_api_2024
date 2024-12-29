# more_python_api

[![](https://img.shields.io/badge/Python-3.12.3-yellow.svg)](https://www.python.org/downloads/) [![](https://img.shields.io/badge/Docker-blue.svg)](https://www.docker.com/) [![](https://img.shields.io/badge/postgres-16.2-blue.svg)](https://hub.docker.com/_/postgres/) [![](https://img.shields.io/badge/serverless-offline-salmon.svg)](https://www.serverless.com/plugins/serverless-offline) 

Run the following from the root dir:

```bash
docker-compose up

# If using Docker Compose Engine V2:
docker compose up
```

## Serverless

Expands on some great examples from: https://github.com/dstilesr/sls-docker-python/blob/master/Dockerfile and https://github.com/aztecweb/docker-serverless-offline.

1. Updates the config.
2. Adds Python dependencies.
3. Some `sls` CLI flags have changed.
4. Adds a Database connection to the example.

* `http://localhost:3001/dev/psqljson` - returns JSON interpolation
* `http://localhost:3001/dev/examples` - returns Examples list from within a Python Serverless function.
* `http://localhost:3001/dev/otherapi` - calls another API deployment (common in layered microservice apps) and returns the retreived value. 

## Fast API

* `http://localhost:8001/examples`
* `http://localhost:8001/` - test/heartbeat endpoint for debugging Docker.

## Postgres

1. The DB will execute scripts in [init_json_sql.sql](postgres/init_json_sql.sql) on initialization.
2. These primarily showcase how to use postgres JSON functionalities ("NoSQL in SQL") and non-rectangular **Record Sets**.

## Resources and Links

1. https://realpython.com/fastapi-python-web-apis/
2. https://github.com/dstilesr/sls-docker-python/blob/master/Dockerfile
3. https://github.com/aztecweb/docker-serverless-offline
4. https://www.serverless.com/plugins/serverless-offline
5. https://stackoverflow.com/questions/40741282/cannot-use-requests-module-on-aws-lambda
