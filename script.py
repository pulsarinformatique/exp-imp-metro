import time
import os
import mysql.connector
import json
import openpyxl
import csv


finalContent = {}

#push in finalContent a new entry

def connect_database(environment="development"):
    """Connect to a MySQL database."""

    connection_config = {
        "development": {
            "host": "localhost",
            "database": "backend_layout",
            "user": "root",
            "password": "root",
            "port": 8889,
        },
        "production": {
            "host": "database.example.com",
            "database": "production",
            "user": "prod_user",
            "password": "prod_password",
            "port": 3306,
        },
    }

    connection_params = connection_config[environment]

    try:
        connection = mysql.connector.connect(
            host=connection_params["host"],
            database=connection_params["database"],
            user=connection_params["user"],
            password=connection_params["password"],
            port=connection_params["port"],
        )
        return connection
    except mysql.connector.Error as error:
        print("Failed to connect to database {}".format(error))




def getAllIdPagesNews(connection):
    try:
        cursor = connection.cursor()
        select = "SELECT title, uid FROM pages WHERE slug LIKE '%actualites%';"
        cursor.execute(select)
        result = cursor.fetchall()
        for row in result:
            getNewsContentByID(connection, row)

        print(finalContent)
    except mysql.connector.Error as error:
        print("Failed to get data from database {}".format(error))


def getNewsContentByID(connection, content):
    try:

        title = content[0]
        uid = content[1]

        cursor = connection.cursor()
        select = f"SELECT bodytext FROM tt_content WHERE pid = {uid}"
        cursor.execute(select)
        results = cursor.fetchall()  # Récupérer tous les résultats
        finalDescription = []
        for description in results:
            #if description == None then pass
            if description[0] == None:
                pass
            else:
                finalDescription.append(description[0])
        
        if len(finalDescription) > 1:
            #join all description in one string
            finalDescription = " ".join(finalDescription)

        finalContent[uid] = {
            "title": title,
            "description": finalDescription
        }
            

    except mysql.connector.Error as error:
        print("Failed to get data from database {}".format(error))

connectDatabase = connect_database("development")
getAllIdPagesNews(connectDatabase)









def readJsonFile():
    try:
        f = open('content.json')
        gedItems = json.load(f)

        for entry in enumerate(gedItems):
            print(entry)
    except mysql.connector.Error as error:
        print("Failed to read json file {}".format(error))


def readJsonFileWithIndex():
    try:
        f = open('content.json')
        gedItems = json.load(f)

        for entry, index in enumerate(gedItems):
            print(entry)
    except mysql.connector.Error as error:
        print("Failed to read json file {}".format(error))



def getPostById(connection, id):
    try:
        cursor = connection.cursor()
        select = f"SELECT * FROM wp_posts WHERE id = {id}"
        cursor.execute(select)
        result = cursor.fetchone()
    except mysql.connector.Error as error:
        print("Failed to get data from database {}".format(error))

def read_csv_file(file_path):
    try:
        with open(file_path, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
            for row in spamreader:
                print(', '.join(row))
    except FileNotFoundError as error:
        print(f"File not found: {error}")
    except Exception as error:
        print(f"An error occurred: {error}")
    
def createPostWpPostAndReturnId(connection):
        actual_time = time.strftime('%Y-%m-%d %H:%M:%S')
        query_post = """
            INSERT INTO wp_posts (
                post_author,
                post_date,
                post_date_gmt,
                post_content,
                post_title,
                post_excerpt,
                post_name,
                to_ping,
                pinged,
                post_modified,
                post_modified_gmt,
                post_content_filtered,
                guid,
                post_type
            ) VALUES (
                1,
                '{}',
                '{}',
                'Mon contenu',
                'Post de clément',
                '',
                'post-de-clement',
                '',
                '',
                '{}',
                '{}',
                '',
                'http://test-python.local/?post_type=product&#038;p=',
                'post'
            )
        """.format(actual_time, actual_time, actual_time)

        try:
            cursor = connection.cursor()
            cursor.execute(query_post)
            connection.commit()
            return cursor.lastrowid
        except mysql.connector.Error as error:
            print("Failed to insert data in database {}".format(error))

    

connectDatabase = connect_database("development")

