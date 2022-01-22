import os
from mysql.connector import connect
from dotenv import load_dotenv


# load environment variables
load_dotenv()


class Database():
    
    def __init__(self):
        self.host = os.getenv('DB_HOST')
        self.user = os.getenv('DB_USER')
        self.password = os.getenv('DB_PASS')
        self.database_name = os.getenv('DB_NAME')
        self.connection = connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database_name
        )
    
    def get_cursor(self):
        cursor = self.connection.cursor()
        return cursor
    
    def create_table(self, sql):
        cursor = self.get_cursor()
        cursor.execute(sql)
        
        self.connection.commit()
        
        print('Successfully created table.')
    
    def select_all(self, table):
        sql = "SELECT * FROM {table}".format(table=table)
        
        cursor = self.get_cursor()
        cursor.execute(sql)
        
        rows = cursor.fetchall()
        
        return rows
    
    def select_by_id(self, table, record_id):
        sql = "SELECT * FROM {table} WHERE id = {record_id}".format(
            table=table, record_id=record_id)
        
        cursor = self.get_cursor()
        cursor.execute(sql)
        
        row = cursor.fetchone()
        
        return row
    
    def select_where(self, table, column, value, limit=None):
        sql = "SELECT * FROM {table} WHERE {column} = %s".format(table=table, column=column)
        
        if limit is not None and type(limit) == int:
            sql += " LIMIT {limit}".format(limit=limit)
        
        values = (value, )
        
        cursor = self.get_cursor()
        cursor.execute(sql, values)
        
        rows = cursor.fetchall()
        
        return rows
    
    def insert(self, table, columns, values):
        sql = "INSERT INTO {table} (".format(table=table)
        
        for column in columns:
            sql += "{column}".format(column=column)
            if columns.index(column) == len(columns) - 1:
                sql += ") VALUES ("
            else:
                sql += ", "
        
        for value in values:
            sql += "%s"
            if values.index(value) == len(values) - 1:
                sql += ")"
            else:
                sql += ", "
        
        if type(values) != tuple:
            values = tuple(value for value in values)
        
        cursor = self.get_cursor()
        cursor.execute(sql, values)
        
        self.connection.commit()
        
        print("Successfully inserted record.")
    
    def update(self, table, columns, values, record_id):
        sql = "UPDATE {table} SET ".format(table=table)
        
        for column in columns:
            sql += "{column} = %s"
            if columns.index(column) == len(columns) - 1:
                sql += " WHERE id = {record_id}".format(record_id, record_id)
            else:
                sql += ", "
        
        if type(values) != tuple:
            values = tuple(value for value in values)
        
        cursor = self.get_cursor()
        cursor.execute(sql, values)
        
        self.connection.commit()
        
        print("Updated record in table {table} with id of {record_id}.".format(table=table, record_id=record_id))
    
    def update_where(self, table, columns, values, cond_column, cond_value):
        sql = "UPDATE {table} SET ".format(table=table)
        
        for column in columns:
            sql += "{column} = %s".format(column=column)
            if columns.index(column) == len(columns) - 1:
                sql += " WHERE {cond_column} = %s".format(cond_column=cond_column)
        
        new_values = []
        for value in values:
            new_values.append(value)
        new_values.append(cond_value)
        
        # convert array to tuple
        new_values = tuple(new_value for new_value in new_values)
        
        cursor = self.get_cursor()
        cursor.execute(sql, values)
        
        self.connection.commit()
        
        print("Successfully updated table where column {cond_column} is equal to {cond_value}".format(
            cond_column=cond_column, cond_value=cond_value))
    
    def delete(self, table, record_id):
        sql = "DELETE FROM {table} WHERE id = {record_id}".format(table=table, record_id=record_id)
        
        cursor = self.get_cursor()
        cursor.execute(sql)
        
        self.connection.commit()
        
        print("Successfully delete record from table {table} with id {record_id}.".format(table=table, record_id=record_id))
    
    def delete_where(self, table, cond_column, cond_value):
        sql = "DELETE FROM {table} WHERE {cond_column} = %s".format(table=table, cond_column=cond_column)
        
        values = None
        if type(cond_value) != tuple:
            values = (cond_value, )
        else:
            values = cond_value
        
        cursor = self.get_cursor()
        cursor.execute(sql, values)
        
        self.connection.commit()
        
        print("Successfully delete records where column {cond_column} is equal to {cond_value}".format(
            cond_column=cond_column, cond_value=cond_value))