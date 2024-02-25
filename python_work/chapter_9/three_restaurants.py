class Restaurant:
    """Restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Creates a restaurant with a name and cuisine type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Prints information"""
        print(f'Name: {self.restaurant_name}')
        print(f'Cuisine Type: {self.cuisine_type}')

    def open_restaurant(self):
        """Opens restaurant"""
        print("Restaurant is open")

restaurant = Restaurant('Pizza Place', 'Italian')
restaurant.describe_restaurant()

restaurant = Restaurant('Chicken Wingz', 'Chicken')
restaurant.describe_restaurant()

restaurant = Restaurant('China House', 'Chinese')
restaurant.describe_restaurant()