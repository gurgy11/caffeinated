import re
from app.lib.database import Database
from app.lib.controller import Controller
from app.modules.users import User


class AuthController(Controller):
    
    def __init__(self):
        super().__init__()
    
    def register(self, form):
        if self.validate_registration_form(form) is False:
            return False
        else:
            name = '{first_name} {last_name}'.format(
                first_name=form.get('first_name'), last_name=form.get('last_name'))
            username = form.get('username')
            email = form.get('email')
            password = form.get('password')
            
            user = User(name, username, email, password)
            values = user.get_insert_values_tuple()
            
            table = 'users'
            columns = ['name', 'username', 'email', 'password']
            
            try:
                self.db.insert(table, columns, values)
            except Exception as e:
                print(str(e))
                self.errors.append('There was an error creating the new user account!')
                return False
            
            return True
    
    def validate_registration_form(self, form):
        ''' Validates the registration form '''
        
        first_name = form.get('first_name')
        last_name = form.get('last_name')
        username = form.get('username')
        email = form.get('email')
        password = form.get('password')
        confirm_password = form.get('confirm_password')
        
        valid = True
        
        if not self.validate_length('first_name', first_name, 3, 16):
            valid = False
        
        if not self.validate_length('last_name', last_name, 3, 16):
            valid = False
        
        if not self.validate_username(username):
            valid = False
        
        if not self.validate_email(email):
            valid = False
        
        if not self.validate_password(password, confirm_password):
            valid = False
        
        return valid
    
    def validate_username(self, username):
        ''' Validates the username field '''
        
        valid = True
        
        if not self.validate_length('username', username, 6, 16):
            valid = False
        
        if not self.validator.contains_digit_character(username):
            self.errors.append('The username field must contain at least one digit!')
            valid = False
        
        return valid
    
    def validate_email(self, email):
        ''' Validates the email field '''
        
        valid = True
        
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        if not re.fullmatch(regex, email):
            self.errors.append('The email address field provided is invalid!')
            valid = False
        
        return valid
    
    def validate_password(self, password, confirm_password):
        ''' Validates the password field '''
        
        valid = True
        
        if password != confirm_password:
            self.errors.append('The password fields must match!')
        
        if not self.validate_length('password', password, 6, 24):
            valid = False
        
        if not self.validator.contains_digit_character(password):
            self.errors.append('The password fields must contain at least one digit!')
            valid = False
        
        if not self.validator.contains_lowercase_character(password):
            self.errors.append('The password fields must contain at least one lowercase character!')
            valid = False
        
        if not self.validator.contains_uppercase_character(password):
            self.errors.append('The password fields must contain at least one uppercase character!')
            valid = False
        
        if not self.validator.contains_special_character(password):
            self.errors.append('The password fields must contain at least one special character!')
            valid = False
        
        return valid