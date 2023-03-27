from mysql import connector
import pandas as pd

"""
Database class:
Helps to create a MySQL database connecting to sepecified user.
It also provides the ability to connect to the database you create if not exists already.

Provides the following methods:

create_table() - create a table in the database.
drop_table() - drop a table from the database.
insert_data() - insert data into a table.
select_data() - select data from a table.
rollback() - roll back a transaction that was previously committed.
close() - close the connection to the database.

This package is based on @mysql and @pandas packages.

Provided by @TweetyX
"""


class Database:

    def __init__(self, username, password, database, host='localhost', port=3306):
        """
        Create & Connect to the database
        :param username: provide your user
        :param password: enter your password to authenticate 
        :param database: the name of the database to create & connect to
        :param host: the host to connect to (default: localhost)
        :param port: the port to connect to (default: 3306)
        """

        try:
            self.conn = connector.connect(
                host=host, user=username, port=port, passwd=password)
            self.cur = self.conn.cursor()
            self.cur.execute(f"CREATE DATABASE IF NOT EXISTS {database}")
            print(f"Database {database} created successfully!!")
            self.cur.execute(f"USE {database}")
            print(f"Connected to {database} successfully!!")
        except connector.Error as e:
            return e

    def create_table(self):
        """
        Create a table with provided name and columns 

        :return: (String) Message of created table successfully or an error message
        """

        # Table data
        table_name = input('Enter the name of the table: ')
        cols_types = input(
            "Enter the columns (separeted with comma) with their data types: ")
        table_name = table_name.strip()
        # Creating the table
        try:
            self.cur.execute("CREATE TABLE IF NOT EXISTS " +
                             table_name+" ("+cols_types+");")
            self.conn.commit()

            return "Table "+table_name+" created!!"
        except connector.Error as e:
            return e

    def drop_table(self, table_name):
        """
        Drop a table

        :param table_name: the name of the table to drop
        :return: (String) Message of dropped table successfully or an error message"""

        try:
            self.cur.execute(f"DROP TABLE IF EXISTS {table_name};")
            self.conn.commit()

            return "Table "+table_name+" dropped!!"
        except connector.Error as e:
            return e

    def insert_data(self, csv, query):
        """
        Insert data into the table

        :param csv: the path to the csv file
        :param query: the query to execute
        :return: (String) Message of inserted data successfully or an error message"""

        data = pd.read_csv(csv)
        data = data.astype(object).where(pd.notnull(data), None)
        try:
            for i, row in data.iterrows():
                self.cur.execute(query, list(row))

            # Saving
            self.conn.commit()
        except connector.Error as e:
            return e


    def select_data(self, table_name):
        """
        Select data from the table

        :param table_name: the name of the table to select
        :return: Selected data successfully or an error message"""

        try:
            self.cur.execute(f"SELECT * FROM {table_name};")
            data = self.cur.fetchall()
            return data
        except connector.Error as e:
            return e

    def rollback(self):
        """
        Rollback the transaction
        """
        self.conn.rollback()
        return None

    def close(self):
        """
        Close the connection to the database
        """
        self.cur.close()
        self.conn.close()
        print("Connection to the database closed successfully!!")
        return None
