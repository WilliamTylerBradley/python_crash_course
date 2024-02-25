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

class IceCreamStand(Restaurant):
    """Ice Cream Stand"""

    def __init__(self, restaurant_name, flavors):
        """Creates a restaurant with a name and cuisine type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = 'Ice Cream'
        self.flavors = flavors

    def display_flavors(self):
        """Display flavors"""
        print('Ice cream flavors:')
        for flavor in self.flavors:
            print(f'- {flavor}')

ice_cream_stand = IceCreamStand('IC', ['Chocolate', 'Vanilla', 'Strawberry'])
ice_cream_stand.display_flavors()