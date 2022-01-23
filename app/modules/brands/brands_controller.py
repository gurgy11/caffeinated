from math import ceil
from flask import session
from app.lib.controller import Controller


class BrandsController(Controller):
    
    def __init__(self):
        super().__init__()
    
    def create(self, form):
        ''' Creates a new brand from a form '''
        
        if not self.validate_create_form(form):
            return False
        else:
            title = form.get('title')
            summary = form.get('summary')
            created_by_id = session.get('user_id')
            
            values = (title, summary, created_by_id, )
            columns = ['title', 'summary', 'created_by_id']
            
            self.db.insert('brands', columns, values)
            
            return True
    
    def validate_create_form(self, form):
        ''' Validates the create form '''
        
        title = form.get('title')
        summary = form.get('summary')
        
        valid = True
        
        if not self.validate_length('title', title, 3, 24):
            valid = False
        
        if not self.validate_length('summary', summary, 0, 600):
            valid = False
        
        if self.already_exists(title):
            self.errors.append('The title field provided already exists!')
            valid = False
        
        return valid
    
    def already_exists(self, title):
        ''' Checks if the title already exists '''
        
        exists = False
        
        results = self.db.select_where('brands', 'title', title)
        if len(results) > 0:
            exists = True
        
        return exists
    
    def fetch_all(self):
        ''' Fetches all brand records '''
        
        results = self.db.select_all('brands')
        brands = []
        
        for res in results:
            brand = {
                'id': res[0],
                'title': res[1],
                'summary': res[2],
                'created_by_id': res[3],
                'created_at': res[4],
                'updated_at': res[5]
            }
            brands.append(brand)
        
        return brands
    
    def delete(self, record_id):
        ''' Deletes a record by id '''
        
        self.db.delete('brands', record_id)
    
    def fetch(self, page, limit):
        ''' Fetches records based on page on amount per page '''
        
        brands = self.fetch_all()
        num_brands = len(brands)
        num_pages = ceil(num_brands / limit)
        offset = (page - 1) * limit
        end_offset = offset + limit
        
        res_brands = []
        
        if page <= 1:
            for b in brands[:limit]:
                res_brands.append(b)
        else:
            for b in brands[offset:end_offset]:
                res_brands.append(b)
        
        return res_brands
    
    def num_pages(self, limit):
        brands = self.fetch_all()
        num_pages = ceil(len(brands) / limit)
        return num_pages