class User:
    """User"""

    def __init__(self, first_name, last_name,
                 location, age):
        """Initialize"""
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.age = age

    def describe_user(self):
        """Describe"""
        description = f'First name: {self.first_name}\n'
        description += f'Last Name: {self.last_name}\n'
        description += f'Location: {self.location}\n'
        description += f'Age: {self.age}\n'
        print(description)
        
    def greet_user(self):
        print(f'Hello, {self.first_name.title()} {self.last_name.title()}')

class Admin(User):
    """Admin"""

    def __init__(self, first_name, last_name,
                 location, age):
        """Init Admin"""
        super().__init__(first_name, last_name,
                 location, age)
        self.privileges = ['Can add post',
                            'Can delete user',
                            'Can ban user']

    def show_privileges(self):
        print(f'Privileges for {self.first_name.title()} {self.last_name.title()}')
        for priviledge in self.privileges:
            print(f'- {priviledge}')

admin_1 = Admin('Tyler', 'Bradley', 'Asheville', 34)
admin_1.show_privileges()