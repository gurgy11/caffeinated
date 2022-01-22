class Model():

    def __init__(self, get_create_table_query=False):
        self._get_create_table_query = get_create_table_query
        self.create_table_query = None
        
        if self._get_create_table_query is True:
            self.get_create_sql_table_query()

    def __init__(self, record_id=None, created_by_id=None, created_at=None, updated_at=None):
        self.record_id = record_id
        self.created_by_id = created_by_id
        self.created_at = created_at
        self.updated_at = updated_at

    ''' Property Setters '''

    def set_record_id(self, record_id):
        self.record_id = record_id
    
    def set_created_by_id(self, created_by_id):
        self.created_by_id = created_by_id

    def set_created_at(self, created_at):
        self.created_at = created_at

    def set_updated_at(self, updated_at):
        self.updated_at = updated_at

    ''' Property Getters '''

    def get_record_id(self):
        return self.record_id
    
    def get_created_by_id(self):
        return self.created_by_id

    def get_created_at(self):
        return self.created_at

    def get_upadted_at(self):
        return self.updated_at

    ''' Helper Methods '''

    def get_dict(self):
        ''' Returns the model as a dictionary object '''

        model = {
            'id': self.record_id,
            'created_by_id': self.created_by_id,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

        return model
    
    def get_create_sql_table_query(self):
        query = '''
        CREATE TABLE IF NOT EXISTS models (
            id INT(11) NOT NULL PRIMARY_KEY AUTO_INCREMENT,
            created_by_id INT(11) NULL,
            created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP(),
            updated_at TIMESTAMP NULL DEFAULT NULL
        )
        '''
        return query
    
    def get_insert_record_sql(self):
        
        sql = """
        INSERT INTO models (id, created_by_id, created_at, updated_at)
        VALUES (%s, %s, %s, %s)
        """
        
        return sql
    
    def get_insert_values_tuple(self):
        record_id = self.record_id
        created_by_id = self.created_by_id
        created_at = self.created_at
        updated_at = self.updated_at
        
        values = (record_id, created_by_id, created_at, updated_at, )
        
        return values
