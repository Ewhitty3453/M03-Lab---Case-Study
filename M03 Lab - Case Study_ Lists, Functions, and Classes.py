class Vehicle:
    def __init__(self):
        self.vehicle_type = ""

    def set_vehicle_type(self, vehicle_type):
        self.vehicle_type = vehicle_type

    def display_info(self):
        print(f"Vehicle type: {self.vehicle_type}")


class Automobile(Vehicle):
    def __init__(self):
        super().__init__()
        self.year = ""
        self.make = ""
        self.model = ""
        self.doors = 0
        self.roof_type = ""

    def get_user_input(self):
        self.year = input("Enter the year: ")
        self.make = input("Enter the make: ")
        self.model = input("Enter the model: ")
        self.doors = int(input("Enter the number of doors (2 or 4): "))
        self.roof_type = input("Enter the type of roof (solid or sun roof): ")

    def display_info(self):
        super().display_info()
        print(f"Year: {self.year}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Number of doors: {self.doors}")
        print(f"Type of roof: {self.roof_type}")


def main():
    automobile = Automobile()

    # Set vehicle type
    vehicle_type = "car"
    automobile.set_vehicle_type(vehicle_type)

    # Get user input
    automobile.get_user_input()

    # Display information
    automobile.display_info()


if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:





# In[ ]:
