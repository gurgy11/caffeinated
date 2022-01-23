from app.lib.model import Model


class Payment(Model):
    
    def __init__(self, customer_id=None, payment_type=None, status=None, details=None, 
                 record_id=None, created_by_id=None, created_at=None, updated_at=None):
        super().__init__(record_id=record_id, created_by_id=created_by_id, 
                         created_at=created_at, updated_at=updated_at)
        self.customer_id = customer_id
        self.payment_type = payment_type
        self.status = status
        self.details = details
    
    ''' Property Getters '''
    
    def get_customer_id(self):
        return self.customer_id
    
    def get_payment_type(self):
        return self.payment_type
    
    def get_status(self):
        return self.status
    
    def get_details(self):
        return self.details
    
    ''' Property Setters '''
    
    def set_customer_id(self, customer_id):
        self.customer_id = customer_id
    
    def set_payment_type(self, payment_type):
        self.payment_type = payment_type
    
    def set_status(self, status):
        self.status = status
    
    def set_details(self, details):
        self.details = details
    
    ''' Helper Methods '''
    
    def get_dict(self):
        
        payment = {
            'id': self.record_id,
            'customer_id': self.customer_id,
            'payment_type': self.payment_type,
            'status': self.status,
            'details': self.details,
            'created_by_id': self.created_by_id,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
        
        return payment
    
    def get_create_sql_table_query(self):
        
        sql = """
        CREATE TABLE IF NOT EXISTS payments (
            id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
            customer_id INT(11) DEFAULT NULL,
            payment_type VARCHAR(45) NOT NULL,
            status VARCHAR(45) NOT NULL,
            details TEXT,
            created_by_id INT(11) DEFAULT NULL,
            created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT NULL,
            CONSTRAINT fk_payment_customer_id
            FOREIGN KEY (customer_id)
                REFERENCES customers(id),
            CONSTRAINT fk_payment_user_id
            FOREIGN KEY (created_by_id)
                REFERENCES users(id)
        );
        """
        
        return sql
    
    def get_insert_values_tuple(self):
        
        customer_id = self.customer_id
        payment_type = self.payment_type
        status = self.status
        details = self.details
        created_by_id = self.created_by_id
        
        values = (customer_id, payment_type, status, details, created_by_id, )
        
        return values