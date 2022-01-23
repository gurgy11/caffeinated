from audioop import add
from app.lib.model import Model


class Customer(Model):
    
    def __init__(self, name=None, email=None, phone=None, address_id=None, notes=None, 
                 record_id=None, created_by_id=None, created_at=None, updated_at=None):
        super().__init__(record_id=record_id, created_by_id=created_by_id, 
                         created_at=created_at, updated_at=updated_at)
        self.name = name
        self.email = email
        self.phone = phone
        self.address_id = address_id
        self.notes = notes
    
    ''' Property Getters '''
    
    def get_name(self):
        return self.name
    
    def get_email(self):
        return self.email
    
    def get_phone(self):
        return self.phone
    
    def get_address_id(self):
        return self.address_id
    
    def get_notes(self):
        return self.notes
    
    ''' Property Setters '''
    
    def set_name(self, name):
        self.name = name
    
    def set_email(self, email):
        self.email = email
    
    def set_phone(self, phone):
        self.phone = phone
    
    def set_address_id(self, address_id):
        self.address_id = address_id
    
    def set_notes(self, notes):
        self.notes = notes
    
    ''' Helper Methods '''
    
    def get_dict(self):
        
        customer = {
            'id': self.record_id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'address_id': self.address_id,
            'notes': self.notes,
            'created_by_id': self.created_by_id,
            'created_at': self.created_at,
            'update_at': self.updated_at
        }
        
        return customer
    
    def get_create_sql_table_query(self):
        
        sql = """
        CREATE TABLE IF NOT EXISTS customers (
            id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(255) NOT NULL,
            phone VARCHAR(20) DEFAULT NULL,
            address_id INT(11) DEFAULT NULL,
            notes TEXT,
            created_by_id INT(11) DEFAULT NULL,
            created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            updated_at NULL TIMESTAMP DEFAULT NULL,
            FOREIGN KEY (address_id) REFERENCES addresses(id),
            FOREIGN KEY (created_by_id) REFERENCES users(id)
        )
        """
        
        return sql
    
    def get_insert_values_tuple(self):
        ''' Returns a tuple of the values for inserting from a form '''
        
        name = self.name
        email = self.email
        phone = self.phone
        address_id = self.address_id
        notes = self.notes
        created_by_id = self.created_by_id
        
        values = (name, email, phone, address_id, notes, created_by_id, )
        
        return values