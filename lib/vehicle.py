class Vehicle:

    def __init__(self, wheel_size, wheel_number):
        self.wheel_size = wheel_size
        self.wheel_number = wheel_number

    def fill_up_tank(self):
        return "filling up!"

# Now you can create instances of the Vehicle class
my_vehicle = Vehicle(48, 4)


