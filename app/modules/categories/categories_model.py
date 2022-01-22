from app.lib.model import Model


class Category(Model):
    
    def __init__(self, get_create_table_query=False):
        self._get_create_table_query = get_create_table_query
        self.create_table_query = None
        
        if self._get_create_table_query is True:
            self.create_table_query = self.get_create_sql_table_query()
    
    def __init__(self, title=None, description=None, parent_id=None, record_id=None, created_by_id=None, 
                 created_at=None, updated_at=None):
        super().__init__(record_id=record_id, created_by_id=created_by_id, 
                         created_at=created_at, updated_at=updated_at)
        self.title = title
        self.description = description
        self.parent_id = parent_id
    
    ''' Property Getters '''
    
    def get_title(self):
        return self.title
    
    def get_description(self):
        return self.description
    
    def get_parent_id(self):
        return self.parent_id
    
    ''' Property Setters '''
    
    def set_title(self, title):
        self.title = title
    
    def set_description(self, description):
        self.description = description
    
    def set_parent_id(self, parent_id):
        self.parent_id = parent_id
    
    ''' Helper Methods '''
    
    def get_dict(self):
        category = {
            'id': self.record_id,
            'title': self.title,
            'description': self.description,
            'parent_id': self.parent_id,
            'created_by_id': self.created_by_id,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
        
        return category
    
    def get_create_sql_table_query(self):
        sql = """
        CREATE TABLE IF NOT EXISTS categories (
            id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(45) NOT NULL,
            description TEXT,
            parent_id INT(11) DEFAULT NULL,
            created_by_id INT(11) DEFAULT NULL,
            created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT NULL,
            CONSTRAINT fk_category_user_id
            FOREIGN KEY (created_by_id)
                REFERENCES users(id)
        )
        """
        
        return sql
    
    def get_insert_record_sql(self):
        sql = """
        INSERT INTO categories (title, description, parent_id, created_by_id)
        VALUES (%s, %s, %s, %s)
        """
        
        return sql
    
    def get_insert_values_tuple(self):
        title = self.title
        description = self.description
        parent_id = self.parent_id
        created_by_id = self.created_by_id
        
        values = (title, description, parent_id, created_by_id, )
        
        return values