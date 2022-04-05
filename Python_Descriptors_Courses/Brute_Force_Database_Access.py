
"""
File: <Brute_Force_Database_Access>.py
-------------------
This snippet will access the database Chinook and grab all the records of the tables Albums and Artists
in order to display them.

"""
import sqlite3


def display_list(list_to_display):
    for record in list_to_display:
        print(record)


def pause():
    # input() waits for a user input
    input("You can't see the next text. (press enter)")


# Driver code
def main():
    db_sqlite_connection = None
    try:
        db_sqlite_connection = sqlite3.connect('chinook.db')  # Connecting to the specific sqlite DB
        cursor = db_sqlite_connection.cursor()  # Get Cursor Object from Connection
        # My queries
        queries_dictionary = {
            "--List all tables--": "SELECT name FROM sqlite_master WHERE type='table';",
            "--List all albums records--": "SELECT * from albums",
            "--List all artists records--": "SELECT * from artists"
        }
        for key, value in queries_dictionary.items():
            print(key)
            cursor.execute(value)  # Retrieving data
            display_list(cursor.fetchall())  # Fetching all rows from the table
            pause()
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)
    finally:
        if db_sqlite_connection:
            db_sqlite_connection.close()  # Closing the connection
            print("The SQLite connection is closed")


# Define main() function for auto test
if __name__ == '__main__':
    # Execute main() function in standalone mode
    main()
