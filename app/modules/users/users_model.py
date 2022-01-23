from audioop import add
from app.lib.model import Model
from werkzeug.security import check_password_hash, generate_password_hash


class User(Model):
    
    def __init__(self, name=None, username=None, email=None, password=None, 
                 phone=None, address_id=None, record_id=None, created_at=None, updated_at=None):
        super().__init__(record_id=record_id, created_at=created_at, updated_at=updated_at)
        self.name = name
        self.username = username
        self.email = email
        self.phone = phone
        self.address_id = address_id
        self.password = password
    
    ''' Property Getters '''
    
    def get_name(self):
        return self.name
    
    def get_username(self):
        return self.username
    
    def get_email(self):
        return self.email
    
    def get_phone(self):
        return self.phone
    
    def get_address_id(self):
        return self.address_id
    
    def get_password(self):
        return self.password
    
    ''' Property Setters '''
    
    def set_name(self, name):
        self.name = name
    
    def set_username(self, username):
        self.username = username
    
    def set_email(self, email):
        self.email = email
    
    def set_phone(self, phone):
        self.phone = phone
    
    def set_address_id(self, address_id):
        self.address_id = address_id
    
    def set_password(self, password):
        self.password = password
    
    ''' Helper Methods '''
    
    def get_dict(self):
        user = {
            'id': self.record_id,
            'name': self.name,
            'username': self.username,
            'email': self.email,
            'phone': self.phone,
            'address_id': self.address_id,
            'password': self.password,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
        
        return user
    
    def set_password_hash(self, password=None):
        if password is None:
            self.password = generate_password_hash(self.password)
        else:
            self.password = generate_password_hash(password)
    
    def check_hashed_password(self, password):
        valid = True
        
        if not check_password_hash(self.password, password):
            valid = False
        
        return valid
    
    def get_create_sql_table_query(self):
        query = '''
        CREATE TABLE IF NOT EXISTS users (
            id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            username VARCHAR(45) NOT NULL,
            email VARCHAR(255) NOT NULL,
            phone VARCHAR(20) DEFAULT NULL,
            address_id INT(11) DEFAULT NULL,
            password VARCHAR(255) NOT NULL,
            created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT NULL
        )
        '''
        
        return query
    
    def get_insert_record_sql(self):
        sql = """
        INSERT INTO users (name, username, email, password)
        VALUES (%s, %s, %s, %s)
        """
        
        return sql
    
    def get_insert_values_tuple(self):
        name = self.name
        username = self.username
        email = self.email
        password = generate_password_hash(self.password)
        
        values = (name, username, email, password)
        
        return values