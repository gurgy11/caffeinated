from app.lib.model import Model


class Order(Model):
    
    def __init__(self, order_items=None, payment_id=None, customer_id=None, shipping_address_id=None, 
                 shipping_cost=None, tax=None, total_price=None, status=None, notes=None, record_id=None, 
                 created_by_id=None, created_at=None, updated_at=None):
        super().__init__(record_id=record_id, created_by_id=created_by_id, 
                         created_at=created_at, updated_at=updated_at)
        self.order_items = order_items
        self.payment_id = payment_id
        self.customer_id = customer_id
        self.shipping_address_id = shipping_address_id
        self.shipping_cost = shipping_cost
        self.tax = tax
        self.total_price = total_price
        self.status = status
        self.notes = notes
    
    ''' Property Getters '''
    
    def get_order_items(self):
        return self.order_items
    
    def get_payment_id(self):
        return self.payment_id
    
    def get_customer_id(self):
        return self.customer_id
    
    def get_shipping_address_id(self):
        return self.shipping_address_id
    
    def get_shipping_cost(self):
        return self.shipping_cost
    
    def get_tax(self):
        return self.tax
    
    def get_total_price(self):
        return self.total_price
    
    def get_status(self):
        return self.status
    
    def get_notes(self):
        return self.notes
    
    ''' Property Setters '''
    
    def set_order_items(self, order_items):
        self.order_items = order_items
    
    def set_payment_id(self, payment_id):
        self.payment_id = payment_id
    
    def set_customer_id(self, customer_id):
        self.customer_id = customer_id
    
    def set_shipping_address_id(self, shipping_address_id):
        self.shipping_address_id = shipping_address_id
    
    def set_shipping_cost(self, shipping_cost):
        self.shipping_cost = shipping_cost
    
    def set_tax(self, tax):
        self.tax = tax
    
    def set_total_price(self, total_price):
        self.total_price = total_price
    
    def set_status(self, status):
        self.status = status
    
    def set_notes(self, notes):
        self.notes = notes
    
    ''' Helper Methods '''
    
    def get_dict(self):
        
        order = {
            'id': self.record_id,
            'order_items': self.order_items,
            'payment_id': self.payment_id,
            'customer_id': self.customer_id,
            'shipping_address_id': self.shipping_address_id,
            'shipping_cost': self.shipping_cost,
            'tax': self.tax,
            'total_price': self.total_price,
            'status': self.status,
            'notes': self.notes,
            'created_by_id': self.created_by_id,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
        
        return order
    
    def get_insert_record_sql(self):
        print('try')
        
        sql = """
        CREATE TABLE IF NOT EXISTS orders (
            id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
            order_items JSON DEFAULT NULL,
            payment_id INT(11) DEFAULT NULL,
            customer_id INT(11) DEFAULT NULL,
            shipping_address_id INT(11) DEFAULT NULL,
            shipping_cost FLOAT DEFAULT NULL,
            tax FLOAT DEFAULT NULL,
            total_price FLOAT DEFAULT NULL,
            status VARCHAR(45) NOT NULL,
            notes TEXT,
            created_by_id INT(11) DEFAULT NULL,
            created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT NULL,
            FOREIGN KEY (payment_id) REFERENCES payments(id),
            FOREIGN KEY (customer_id) REFERENCES customers(id),
            FOREIGN KEY (shipping_address_id) REFERENCES addresses(id),
            FOREIGN KEY (created_by_id) REFERENCES users(id)
        );
        """
        
        return sql
    
    def get_insert_values_tuple(self):
        
        order_items = self.order_items
        payment_id = self.payment_id
        customer_id = self.customer_id
        shipping_address_id = self.shipping_address_id
        shipping_cost = self.shipping_cost
        tax = self.tax
        total_price = self.total_price
        status = self.status
        notes = self.notes
        created_by_id = self.created_by_id
        
        values = (order_items, payment_id, customer_id, shipping_address_id, shipping_cost, 
                  tax, total_price, status, notes, created_by_id)
        
        return values