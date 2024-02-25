class Employee:
    """Employee"""

    def __init__(self, first_name, last_name, salary):
        """Initialize employee"""
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, amount = 5000):
        """Increase salary by amount"""
        self.salary += amount