OnlineFoodOrderingSystem
====

This project simulate online food order process.

It has three models: restaurant, menu, and item in menu

# Prerequisites:

Ubuntu

Flask

Flask_restful

boto3

dynamodb

# File description:
- setup.py: create database tables

- server.py: provide REST api

- client.py: send HTTP requests

- test.py: unit test for the 4 http methods: POST, GET, PUT, DELETE

# How to run it:

go to dynamodb folder and run:

```java -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar -sharedDb```

create database tables:

```python setup.py```

start server:

```python server.py```

run test:

```python test.py```


