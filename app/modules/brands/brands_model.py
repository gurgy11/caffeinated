from app.lib.model import Model


class Brand(Model):
    
    def __init__(self, get_create_table_query=False):
        self._get_create_table_query = get_create_table_query
        self.create_table_query = None
        
        if self._get_create_table_query is True:
            self.create_table_query = self.get_create_sql_table_query()
    
    def __init__(self, title=None, summary=None, notes=None, record_id=None, created_by_id=None, created_at=None, updated_at=None):
        super().__init__(record_id=record_id, created_by_id=created_by_id,
                         created_at=created_at, updated_at=updated_at)
        self.title = title
        self.summary = summary
        self.notes = notes
    
    ''' Property Setters '''
    
    def set_title(self, title):
        self.title = title
    
    def set_summary(self, summary):
        self.summary = summary
    
    ''' Property Getters '''
    
    def get_title(self):
        return self.title
    
    def get_summary(self):
        return self.summary
    
    ''' Helper Methods '''
    
    def get_dict(self):
        ''' Returns the brand model as a dict '''
        
        brand = {
            'id': self.record_id,
            'title': self.title,
            'summary': self.summary,
            'created_by_id': self.created_by_id,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
        
        return brand
    
    def get_create_sql_table_query(self):
        query = """
        CREATE TABLE IF NOT EXISTS brands (
            id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(45) NOT NULL,
            summary TEXT DEFAULT NULL,
            created_by_id INT(11) NULL,
            created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP NULL ON UPDATE CURRENT_TIMESTAMP,
            CONSTRAINT fk_brand_user_id FOREIGN KEY (created_by_id)
            REFERENCES users(id)
        );"""
        
        return query