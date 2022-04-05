
"""
File: <Descriptors_Database_Access>.py
    -------------------
    This snippet will access the database Chinook and grab all the records of the tables Albums and Artists
    in order to display them by using descriptors

    self is the instance of the descriptor you create.
    object is the instance of the object your descriptor is attached.
    type is the type of the object the descriptor is attached to.

    value is the value that is assigned to the attribute of the descriptor.
    get(self, object, type) set(self, object, value)
    delete(self, object)

    __get__() accesses the attribute or when you want to extract some information. It returns the value of the attribute
    or raises the AttributeError exception if a requested attribute is not present.

    __set__() is called in an attribute assignment operation that sets the value of an attribute. Returns nothing.
    But can raise the AttributeError exception.

    __delete__() controls a delete operation, i.e., when you would want to delete the attribute from an object.
     Returns nothing.


"""


import sqlite3


class Descriptor:
    """
        A data descriptor that sets, deletes and returns values
        The SQL operations are not the objectives here.
        The aim was to build a Descriptor with basic magic methods
    """
    def __get__(self, obj, objtype=None):
        """ Returns a row of data from a table with a specific PK """
        try:
            desc_connection = obj.active_connection  # Getting the active connection from the calling instance object
            desc_cursor = desc_connection.cursor()  # Getting the active cursor from the calling instance object
            table_data = desc_cursor.execute("SELECT * FROM " + str(obj.table))  # Getting the list of all columns
            pk_column = table_data.description[0][0]  # Getting the primary key column from the structure
            select_query = "SELECT * from " + str(obj.table) + " WHERE " + str(pk_column) + " = " \
                           + str(obj.primary_key)  # Building the SQL Query
            desc_cursor.execute(select_query)  # Retrieving data
            return desc_cursor.fetchone()
            # return desc_cursor.fetchall()  # Fetching all rows from the table
            # return desc_cursor.execute(select_query)
        except sqlite3.Error as error:
            print("Failed to get data from sqlite table", error)

    def __set__(self, obj, value):
        """ Inserts a row to the table  """
        open_str = "("
        close_str = ")"
        values_to_add = ""

        for i_ndex in range(0, len(value)):  # This loop will do the concatenation of elements to be added to the table
            if i_ndex == (len(value) - 1):  # Making sure it's the last element of the list to add a semicolon
                values_to_add = values_to_add + str(value[i_ndex])
            else:  # Adding a comma at the end of each element until the last one
                values_to_add = values_to_add + value[i_ndex] + "," + " "
        values_to_add = open_str + values_to_add + close_str + ";"
        try:
            desc_connection = obj.active_connection  # Getting the active connection from the calling instance object
            desc_cursor = desc_connection.cursor()  # Getting the active cursor from the calling instance object
            table_data = desc_cursor.execute("SELECT * FROM " + str(obj.table))  # Getting the list of all columns
            column_to_insert = ''
            if len(table_data.description) > 2:
                for i_ndex in range(1, len(table_data.description)):
                    if i_ndex == (len(table_data.description) - 1):
                        column_to_insert = column_to_insert + str(table_data.description[i_ndex][0])
                    else:
                        column_to_insert = column_to_insert + str(table_data.description[i_ndex][0]) + ", "
            else:
                column_to_insert = table_data.description[1][0]

            insert_query = "INSERT INTO " + obj.table + " " + open_str + column_to_insert + close_str + " VALUES " \
                           + values_to_add
            desc_cursor.execute(insert_query)  # Adding a new record  ---- The executemany could be used too ----
            desc_connection.commit()  # Commit the new rows to the table
            print("Record(s) inserted successfully:", desc_cursor.rowcount)
            desc_cursor.close()  # Closing the cursor
            obj.primary_key = desc_cursor.lastrowid  # Getting the PKI to make sure we keep track of the record
        except sqlite3.Error as error:
            print("Failed to insert data into sqlite table", error)

    def __delete__(self, obj):
        """ Deletes a row based on the PK (obj.primary_key) of the current object """
        try:
            desc_connection = obj.active_connection  # Getting the active connection from the calling instance object
            desc_cursor = desc_connection.cursor()  # Getting the active cursor from the calling instance object
            table_data = desc_cursor.execute("SELECT * FROM " + str(obj.table))  # Getting the list of all columns
            pk_column = table_data.description[0][0]  # Getting the primary key column from the structure
            delete_query = "DELETE FROM " + str(obj.table) + " WHERE " + str(pk_column) + " = " \
                           + str(obj.primary_key)  # Building the SQL Query
            desc_cursor.execute(delete_query)  # Deleting the data
            # Deleting single record now
            desc_cursor.execute(delete_query)
            desc_connection.commit()
            print("Record deleted successfully ")
            desc_cursor.close()
        except sqlite3.Error as error:
            print("Failed to delete record from sqlite table", error)


class Database:
    """
        Database class tha holds all the major database operations
    """
    _active_connection = None
    _active_cursor = None

    def __init__(self, db_path):
        """Initialize db class variables"""
        self.db_path = db_path
        if not self._active_connection:
            try:
                self._active_connection = sqlite3.connect(self.db_path)  # Connecting to the specific sqlite DB
                self._active_cursor = self._active_connection.cursor()  # Retrieving data
                # Retrieving the list of tables in the DB
                print("The list of all tables")
                display_list(self._active_cursor.execute("SELECT name FROM sqlite_master WHERE type='table'"))
                # print(f"The list of all tables : {self._active_cursor.fetchall()}")  # Fetching all tables from the DB
                print("\n")
            except sqlite3.Error as error:
                print("Error while connecting to sqlite", error)

    def close(self):
        """close sqlite3 connection"""
        if self._active_connection:
            self._active_connection.close()
            self._active_connection = None
            print("The SQLite connection is closed")

    @property
    def connected(self):  # Getting the active connection at hand for further use
        return self._active_connection

    @property
    def cursor(self):  # Getting the active connection at hand for further use
        return self._active_cursor


class Record:
    record = Descriptor()

    def __init__(self, active_connection, table, primary_key=None):
        self.active_connection = active_connection
        self.table = table
        if primary_key:  # Specifying a record
            self.primary_key = int(primary_key)
        else:
            # raise Exception("The primary key is missing")
            self.primary_key = None


def display_list(list_to_display):
    for record in list_to_display:
        print(record)


def main():  # Driver code

    obj_db = Database("chinook.db")  # Creating the Database Object
    """
        Albums Table
    """
    print("ALBUMS OPERATIONS")
    obj_record_from_albums_1 = Record(obj_db.connected, "Albums", 50)  # Getting the record object from the database
    print(obj_record_from_albums_1.record)  # Call the __get__ method of the Descriptor
    obj_record_from_albums_2 = Record(obj_db.connected, "Albums")  # Empty object of type Artist
    obj_record_from_albums_2.record = ["\"New Album 2\"", 14]  # Call the __set__ method of the Descriptor
    obj_record_from_albums_3 = Record(obj_db.connected, "Albums", 318)  # Call the __get__ method of the Descriptor
    obj_record_from_albums_4 = Record(obj_db.connected, "Albums", 320)  # Call the __get__ method of the Descriptor
    del obj_record_from_albums_3.record  # Call the __delete__ method of the Descriptor
    del obj_record_from_albums_4.record  # Call the __delete__ method of the Descriptor

    """
           Artists Table
    """
    print("ARTISTS OPERATIONS")
    # Creating a new Artist
    obj_record_from_artists_1 = Record(obj_db.connected, "Artists", 294)  # Getting the record object from the database
    print(obj_record_from_artists_1.record)  # Call the __get__ method of the Descriptor
    obj_record_from_artists_2 = Record(obj_db.connected, "Artists")  # Empty object of type Artist
    obj_record_from_artists_3 = Record(obj_db.connected, "Artists")  # Empty object of type Artist
    obj_record_from_artists_4 = Record(obj_db.connected, "Artists")  # Empty object of type Artist
    obj_record_from_artists_5 = Record(obj_db.connected, "Artists")  # Empty object of type Artist
    obj_record_from_artists_2.record = ["\"New Artist 2\""]  # Call the __set__ method of the Descriptor
    obj_record_from_artists_3.record = ["\"New Artist 3\""]  # Call the __set__ method of the Descriptor
    obj_record_from_artists_4.record = ["\"New Artist 4\""]  # Call the __set__ method of the Descriptor
    obj_record_from_artists_5.record = ["\"New Artist 5\""]  # Call the __set__ method of the Descriptor
    obj_record_from_artists_45 = Record(obj_db.connected, "Artists", 318)  # Call the __get__ method of the Descriptor
    obj_record_from_artists_47 = Record(obj_db.connected, "Artists", 320)  # Call the __get__ method of the Descriptor
    del obj_record_from_artists_45.record  # Call the __delete__ method of the Descriptor
    del obj_record_from_artists_47.record  # Call the __delete__ method of the Descriptor

    obj_db.close()


# Define main() function for auto test
if __name__ == '__main__':
    # Execute main() function in standalone mode
    main()