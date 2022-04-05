"""
File: <Class_Database_Access>.py
-------------------
This snippet will access the database Chinook and grab all the records of the tables Albums and Artists
in order to display them by using classes

"""

import sqlite3


class Database:
    """
        Database class tha holds all the major database operations
    """
    DB_LOCATION = "chinook.db"
    _active_connection = None
    _active_cursor = None

    def __init__(self):
        """Initialize db class variables"""
        if not self._active_connection:
            try:
                self._active_connection = sqlite3.connect(Database.DB_LOCATION)  # Connecting to the specific sqlite DB
                self._active_cursor = self._active_connection.cursor()  # Retrieving data

            except sqlite3.Error as error:
                print("Error while connecting to sqlite", error)

    def close(self):
        """close sqlite3 connection"""
        if self._active_connection:
            if self._active_connection:
                self._active_connection.close()
                print("The SQLite connection is closed")

    def execute(self, query):
        """execute a row of data to current cursor"""
        self._active_cursor.execute(query)  # Retrieving data
        return self._active_cursor.fetchall()  # Fetching all rows from the table


def display_list(list_to_display):
    for record in list_to_display:
        print(record)


# Driver code
def main():
    obj_db = Database()
    display_list(obj_db.execute("SELECT name FROM sqlite_master WHERE type='table'"))
    display_list(obj_db.execute("SELECT * from albums"))
    display_list(obj_db.execute("SELECT * from artists"))
    display_list(obj_db.execute("SELECT * from employees"))
    obj_db.close()


# Define main() function for auto test
if __name__ == '__main__':
    # Execute main() function in standalone mode
    main()
