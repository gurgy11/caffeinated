from app.lib.model import Model


class Address(Model):
    
    def __init__(self, get_create_table_query=False):
        self._get_create_table_query = get_create_table_query
        self.create_table_query = None
        
        if self._get_create_table_query is True:
            self.create_table_query = self.get_create_sql_table_query()
    
    def __init__(self, street_address=None, city=None, postal_zip=None, province_state=None, country=None,
                 record_id=None, created_by_id=None, created_at=None, updated_at=None):
        super().__init__(record_id=record_id, created_by_id=created_by_id,
                         created_at=created_at, updated_at=updated_at)
        self.street_address = street_address
        self.city = city
        self.postal_zip = postal_zip
        self.province_state = province_state
        self.country = country
    
    ''' Property Getters '''
    
    def get_street_address(self):
        return self.street_address
    
    def get_city(self):
        return self.city
    
    def get_postal_zip(self):
        return self.postal_zip
    
    def get_province_state(self):
        return self.province_state
    
    def get_country(self):
        return self.country
    
    ''' Property Setters '''
    
    def set_street_address(self, street_address):
        self.street_address = street_address
    
    def set_city(self, city):
        self.city = city
    
    def set_postal_zip(self, postal_zip):
        self.postal_zip = postal_zip
    
    def set_province_state(self, province_state):
        self.province_state = province_state
    
    def set_country(self, country):
        self.country = country
    
    ''' Helper Methods '''
    
    def get_dict(self):
        address = {
            'id': self.record_id,
            'street_address': self.street_address,
            'city': self.city,
            'postal_zip': self.postal_zip,
            'province_state': self.province_state,
            'country': self.country,
            'created_by_id': self.created_by_id,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
        
        return address
    
    def get_create_sql_table_query(self):
        query = """
        CREATE TABLE IF NOT EXISTS addresses (
            id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
            street_address VARCHAR(120) NOT NULL,
            city VARCHAR(45) NOT NULL,
            postal_zip VARCHAR(20) NOT NULL,
            province_state VARCHAR(45) NOT NULL,
            country VARCHAR(45) NOT NULL,
            created_by_id INT(11) NULL DEFAULT NULL,
            created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP NULL DEFAULT NULL,
            CONSTRAINT fk_address_user_id
            FOREIGN KEY (created_by_id)
                REFERENCES users(id)
        )
        """
        
        return query
    
    def get_insert_record_sql(self):
        sql = """
        INSERT INTO addresses (street_address, city, postal_zip, province_state, country, created_by_id)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        
        return sql
    
    def get_insert_values_tuple(self):
        street_address = self.street_address
        city = self.city
        postal_zip = self.postal_zip
        province_state = self.province_state
        country = self.country
        created_by_id = self.created_by_id
        
        values = (street_address, city, postal_zip, province_state, country, created_by_id, )
        
        return values