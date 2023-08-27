from vehicle import Vehicle

class Car:
    def __init__(self, wheel_size, wheel_number):
        self.wheel_size = wheel_size
        self.wheel_number = wheel_number

class Car(Vehicle):  # Assuming Car is a subclass of Vehicle
    def go(self):
        return "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"

# Now you can create instances of the Car class
my_car = Car(48, 4)
