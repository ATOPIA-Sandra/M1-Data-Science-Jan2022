
"""
File: <Property_Database_Access>.py
-------------------
This snippet will access the database Chinook and grab all the records of the tables Albums and Artists
in order to display them by using descriptors

"""

import sqlite3


class Database:
    """
            Database class tha holds all the major database operations
    """
    _active_connection = None
    _active_cursor = None

    def __init__(self, db_path, table):
        """Initialize db class variables"""
        self.db_path = db_path
        self.__table = table
        if not self._active_connection:
            try:
                self._active_connection = sqlite3.connect(self.db_path)  # Connecting to the specific sqlite DB
                self._active_cursor = self._active_connection.cursor()  # Retrieving data
                # Retrieving the list of tables in the DB
                self._active_cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
                print(f"The list of all tables : {self._active_cursor.fetchall()}")  # Fetching all tables from the DB
                print("\n")
            except sqlite3.Error as error:
                print("Error while connecting to sqlite", error)

    @property
    def table(self):
        """execute a row of data to current cursor"""
        query = "SELECT * from " + self.__table
        self._active_cursor.execute(query)  # Retrieving data
        return self._active_cursor.fetchall()  # Fetching all rows from the table

    @table.setter
    def table(self, table):
        pass

    def close(self):
        """close sqlite3 connection"""
        if self._active_connection:
            self._active_connection.close()
            self._active_connection = None
            print("The SQLite connection is closed")


def display_list(list_to_display):
    for record in list_to_display:
        print(record)


def main():  # Driver code
    obj_db = Database("chinook.db", "artists")
    display_list(obj_db.table)
    obj_db.table = "albums"
    display_list(obj_db.table)
    obj_db.table = "employees"
    display_list(obj_db.table)
    obj_db.close()


# Define main() function for auto test
if __name__ == '__main__':
    # Execute main() function in standalone mode
    main()