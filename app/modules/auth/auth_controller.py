import re
from app.lib.database import Database
from app.lib.controller import Controller
from app.modules.users import User
from app.lib.authentication import set_user_session


class AuthController(Controller):
    
    def __init__(self):
        super().__init__()
        
    def login(self, form):
        ''' Processes the login form, returning True if valid, otherwise it returns False, indicating errors '''
        
        if self.validate_login_form(form):
            return True
        else:
            return False
    
    def validate_login_form(self, form):
        ''' Validates the login and makes sure the credentials are correct, returning True or False if the form is valid '''
        
        self.errors.clear()
        valid = True
        
        username = form.get('username')
        password = form.get('password')
        
        if self.username_exists(username) is True:
            results = self.db.select_where('users', 'username', username)
            if len(results) > 0:
                user_result = results[0]
                
                result_username = user_result[2]
                result_password = user_result[6]
                
                user = User(username=result_username, password=result_password)
                
                # check if password matches
                if not user.check_hashed_password(password):
                    self.errors.append('The password provided is incorrect!')
                    valid = False
                else:
                    # set the user in the session
                    set_user_session(user_result[0], result_username)
        else:
            self.errors.append('The username provided does not exist!')
            valid = False
        
        return valid
    
    def register(self, form):
        ''' Registers a new user if there are not form errors and returns True, if there are errors, it returns False '''
        
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
        
        self.errors.clear()
        valid = True
        
        if not self.validate_length('first name', first_name, 3, 16):
            valid = False
        
        if not self.validate_length('last name', last_name, 3, 16):
            valid = False
        
        if not self.validate_username(username):
            valid = False
        
        if self.username_exists(username) is True:
            self.errors.append('The username provided is already registered to an existing account!')
            valid = False
        
        if not self.validate_email(email):
            valid = False
        
        if self.email_exists(email) is True:
            self.errors.append('The email address provided is already registered to an existing account!')
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
        
        try:
            regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
            if not re.fullmatch(regex, str(email)):
                self.errors.append('The email address field provided is invalid!')
                valid = False
        except Exception as e:
            self.errors.append('An error occurred while validating the email address provided!')
            print(str(e))
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
    
    def username_exists(self, username):
        ''' Returns True if the username exists, otherwise, it returns False '''
        
        exists = False
        
        results = self.db.select_where('users', 'username', username)
        
        if len(results) > 0:
            exists = True
        
        return exists
    
    def email_exists(self, email):
        ''' Returns True if the email exists, otherwise, returns False '''
        
        exists = False
        
        results = self.db.select_where('users', 'email', email)
        
        if len(results) > 0:
            exists = True
        
        return exists