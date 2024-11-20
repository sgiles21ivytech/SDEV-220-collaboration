# Part 1 of Case Study. Test Case should produce all attributes from both the Parent and child class.

class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
    
    def __str__(self):
        return f"Vehicle type: {self.vehicle_type}\n" \
               f"  Year: {self.year}\n" \
               f"  Make: {self.make}\n" \
               f"  Model: {self.model}\n" \
               f"  Number of doors: {self.doors}\n" \
               f"  Type of roof: {self.roof}" 

    """
    Apart of Test Case
    def __str__(self):
        return f"My favorite Automobile is a {self.vehicle_type}. For some reason \n" \
               f"the {self.year} {self.make} {self.model} has been my personal favorite. \n" \
               f"It's a {self.doors} door and a very comfortable ride! One of the best {self.roof}s I've ever had!
               """

# Test Case
#favorite_car = Automobile("Car", 2023, "Porsche", "Cayenne E-Hybrid", 4, "sunroof")
#print(favorite_car)

"""////////////////////////////////////////////////////////////////////////////////////"""

# Part 2 of Case Study. This part of the program will allow accept user input for a vehicle with the Main Method.

def main():
    vehicle_type = "car" 

    year = int(input("Enter the year: "))
    make = input("Enter the make: ")
    model = input("Enter the model: ")
    doors = int(input("Enter the number of doors: "))
    roof = input("Enter the type of roof: ")

    car = Automobile(vehicle_type, year, make, model, doors, roof)
    print(car)

if __name__ == "__main__":
    main()









        