import os

from mysql.connector import connect, Error
from dotenv import load_dotenv

from .database import Database

# import models
from app.modules.addresses import Address
from app.modules.brands import Brand
from app.modules.categories import Category
from app.modules.customers import Customer
from app.modules.employees import Employee
from app.modules.orders import Order
from app.modules.payments import Payment
from app.modules.users import User


class Initializer():
    
    load_dotenv()
    
    def __init__(self):
        self.db = Database()
        self.initialize_database()
    
    def initialize_database(self):
        connection = connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASS')
        )
        
        sql = "CREATE DATABASE IF NOT EXISTS {db_name}".format(db_name=os.getenv('DB_NAME'))
        
        cursor = connection.cursor()
        cursor.execute(sql)
        
        connection.commit()
        
        self.initialize_tables()
    
    def initialize_tables(self):
        
        # User
        user = User()
        users_sql = user.get_create_sql_table_query()
        self.db.create_table(users_sql)
        
        # addresses
        address = Address()
        addresses_sql = address.get_create_sql_table_query()
        self.db.create_table(addresses_sql)
        
        # brands
        brand = Brand()
        brands_sql = brand.get_create_sql_table_query()
        self.db.create_table(brands_sql)
        
        # Category
        category = Category()
        categories_sql = category.get_create_sql_table_query()
        self.db.create_table(categories_sql)
        
        # Customer
        customer = Customer()
        customers_sql = customer.get_create_sql_table_query()
        self.db.create_table(customers_sql)
        
        # Payment
        payment = Payment()
        payments_sql = payment.get_create_sql_table_query()
        self.db.create_table(payments_sql)
        
        # Order
        try:
            order = Order()
            orders_sql = order.get_create_sql_table_query()
            self.db.create_table(orders_sql)
        except Error as e:
            print(str(e))
        
        # Employee
        employee = Employee()
        employees_sql = employee.get_create_sql_table_query()
        self.db.create_table(employees_sql)