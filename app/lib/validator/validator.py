class Validator():
    
    def __init__(self):
        self.special_symbols = ['!', '@', '#', '$', '%']
    
    def valid_min_length(self, value, min_length):
        ''' Validate a values minimum length '''
        
        valid = True
        
        if len(value) < min_length:
            valid = False
        
        return valid
    
    def valid_max_length(self, value, max_length):
        ''' Validate a values maximum length '''
        
        valid = True
        
        if len(value) > max_length:
            valid = False
        
        return valid
    
    def contains_lowercase_character(self, value):
        ''' Validates a value for at least 1 lowercase character '''
        
        valid = True
        
        if not any(char.islower() for char in value):
            valid = False
        
        return valid
    
    def contains_uppercase_character(self, value):
        ''' Validates a value for at least 1 uppercase character '''
        
        valid = True
        
        if not any(char.isupper() for char in value):
            valid = False
        
        return valid
    
    def contains_digit_character(self, value):
        ''' Validates a value for at least 1 digit '''
        
        valid = True
        
        if not any(char.isdigit() for char in value):
            valid = False
        
        return valid
    
    def contains_special_character(self, value, special_chars=None):
        ''' Validates a value for at least one special character '''
        
        valid = True
        
        if special_chars is not None:
            self.special_symbols = special_chars
        
        if not any(self.special_symbols for val in value):
            valid = False
        
        return valid