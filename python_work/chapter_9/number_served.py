class Restaurant:
    """Restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Creates a restaurant with a name and cuisine type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Prints information"""
        print(f'Name: {self.restaurant_name}')
        print(f'Cuisine Type: {self.cuisine_type}')

    def open_restaurant(self):
        """Opens restaurant"""
        print("Restaurant is open")

    def set_number_served(self, number):
        """Set number served"""
        self.number_served = number

    def increment_number_served(self, increment):
        """Increase number served"""
        self.number_served += increment

restaurant = Restaurant('Pizza Place', 'Italian')

print(restaurant.number_served)

restaurant.set_number_served(10)

print(restaurant.number_served)

restaurant.increment_number_served(10)

print(restaurant.number_served)