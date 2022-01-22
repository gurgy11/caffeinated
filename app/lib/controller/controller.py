from app.lib.database import Database
from app.lib.validator import Validator


class Controller():
    
    def __init__(self):
        self.db = Database()
        self.validator = Validator()
        self.errors = []
    
    def validate_length(self, field, value, min_length, max_length):
        ''' Validates a values minimum and maximum length '''
        
        valid = True
        
        if not self.validator.valid_min_length(value, min_length):
            self.errors.append('The {field} must be at least {min_length} characters long!'.format(
                field=field, min_length=min_length))
            valid = False
        
        if not self.validator.valid_max_length(value, max_length):
            self.errors.append('The {field} cannot exceed {max_length} characters long!'.format(
                field=field, max_length=max_length
            ))
            valid = False
        
        return valid