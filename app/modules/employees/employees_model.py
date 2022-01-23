from app.lib.model import Model


class Employee(Model):
    
    def __init__(self, name=None, email=None, phone=None, address_id=None, 
                 role=None, salary=None, salary_unit=None, status=None, notes=None,
                 record_id=None, created_by_id=None, created_at=None, updated_at=None):
        super().__init__(record_id=record_id, created_by_id=created_by_id, 
                         created_at=created_at, updated_at=updated_at)
        self.name = name
        self.email = email
        self.phone = phone
        self.address_id = address_id
        self.role = role
        self.salary = salary
        self.salary_unit = salary_unit # is the salary entered hourly? weekly? monthly? yearly?
        self.status = status
        self.notes = notes
    
    ''' Property Getters '''
    
    def get_name(self):
        return self.name
    
    def get_email(self):
        return self.email
    
    def get_phone(self):
        return self.phone
    
    def get_address_id(self):
        return self.address_id
    
    def get_role(self):
        return self.role
    
    def get_salary(self):
        return self.salary
    
    def get_salary_unit(self):
        return self.salary_unit
    
    def get_status(self):
        return self.status
    
    def get_notes(self):
        return self.notes
    
    ''' Property Setters '''
    
    def set_name(self, name):
        self.name = name
    
    def set_email(self, email):
        self.email = email
    
    def set_phone(self, phone):
        self.phone = phone
    
    def set_address_id(self, address_id):
        self.address_id = address_id
    
    def set_role(self, role):
        self.role = role
    
    def set_salary(self, salary):
        self.salary = salary
    
    def set_salary_unit(self, salary_unit):
        self.salary_unit = salary_unit
    
    def set_status(self, status):
        self.status = status
    
    def set_notes(self, notes):
        self.notes = notes
    
    ''' Helper Methods '''
    
    def get_dict(self):
        
        employee = {
            'id': self.record_id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'address_id': self.address_id,
            'role': self.role,
            'salary': self.salary,
            'salary_unit': self.salary_unit,
            'status': self.status,
            'notes': self.notes,
            'created_by_id': self.created_by_id,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
        
        return employee
    
    def get_create_sql_table_query(self):
        
        sql = """
        CREATE TABLE IF NOT EXISTS employees (
            id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(255) NOT NULL,
            phone VARCHAR(20) DEFAULT NULL,
            address_id INT(11) DEFAULT NULL,
            role VARCHAR(45) DEFAULT NULL,
            salary FLOAT DEFAULT NULL,
            salary_unit VARCHAR(45) DEFAULT NULL,
            status VARCHAR(45) DEFAULT NULL,
            notes TEXT,
            created_by_id INT(11) DEFAULT NULL,
            created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT NULL,
            CONSTRAINT fk_employee_address_id
            FOREIGN KEY (address_id)
                REFERENCES addresses(id),
            CONSTRAINT fk_employee_user_id
            FOREIGN KEY (created_by_id)
                REFERENCES users(id)
        )
        """
        
        return sql
    
    def get_insert_values_tuple(self):
        
        name = self.name
        email = self.email
        phone = self.phone
        address_id = self.address_id
        role = self.role
        salary = self.salary
        salary_unit = self.salary_unit
        status = self.status
        notes = self.notes
        created_by_id = self.created_by_id
        
        values = (name, email, phone, address_id, role, salary, salary_unit, status, notes, created_by_id, )
        
        return values