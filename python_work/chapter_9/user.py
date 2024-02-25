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

user_1 = User('Tyler', 'Bradley', 'Asheville', 34)
user_1.describe_user()
user_1.greet_user()