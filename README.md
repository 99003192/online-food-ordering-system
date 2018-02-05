Online Food Ordering System (REST API)
====

This project simulates online food order process.

It has three types of objects: restaurant, menu, and item in menu. 
Each restaurant can have 0 to many menus associated with it (breakfast, lunch, dinner, etc.).
Each menu can have 0 to many menu items associated with it.

This project uses Flask to host REST server and DynamoDB as the data storage.

# Prerequisites:

- Required OS: Ubuntu (tested version: 14.04.5 LTS; other versions should also work)

    Required Language: Python 2.X or 3.X

- Install required Python libraries:

    `sudo pip install requests Flask Flask-RESTful boto3`

- Set up DynamoDB Local (Downloadable Version):

    - Download and unzip DynamoDB: 
        ```
        wget https://s3-us-west-2.amazonaws.com/dynamodb-local/dynamodb_local_latest.zip 
        unzip dynamodb_local_latest.zip -d dynamodb
        ```
        (Note: To run DynamoDB on your computer, you must have the Java Runtime Environment (JRE) version 6.x or newer. 
        To install JRE:  `sudo apt-get install default-jre`)
    - Configure AWS:
    
        Install AWS Command Line Interface (CLI): `sudo apt-get install awscli`
        
        Configure AWS using CLI:
        ```
        aws configure
        AWS Access Key ID [None]: AKIAJEV6NKQCHAUZPCTQ
        AWS Secret Access Key [None]: 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
        Default region name [None]: us-east-2
        Default output format [None]: ENTER
        ```

- Download project code: `git clone https://github.com/mkuai/online-food-ordering-system.git`

# File description:

- setup.py: create database tables

- server.py: provide REST API

- client.py: send HTTP requests

- test.py: unit test for the 4 HTTP methods: POST, GET, PUT, DELETE

# How to run it:

 - Run DynamoDB
     ```
     # open a terminal
     cd dynamodb
     java -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar -sharedDb
     ```
- Create database tables
    ```
    # open a terminal
    cd online-food-ordering-system
    python setup.py
    ```
- Run server:
    ```
    python server.py
    ```
- Run client:
    ```
    # open a terminal
    cd online-food-ordering-system
    python client.py
    ```
- Run unit test:
    ```
    python test.py
    ```