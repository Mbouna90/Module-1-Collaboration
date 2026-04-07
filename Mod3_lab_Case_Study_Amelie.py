
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

# Step 2: Define the subclass that inherits from Vehicle
class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        # super().__init__ links this class to the Vehicle superclass
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

def main():
    # Step 3: Accept user input
    print("--- Enter Vehicle Information ---")
    # Fixed as "car" per assignment requirements
    v_type = "car"
    
    year = input("Enter the year: ")
    make = input("Enter the make: ")
    model = input("Enter the model: ")
    doors = input("Enter number of doors (2 or 4): ")
    roof = input("Enter type of roof (solid or sun roof): ")

    # Step 4: Create the Automobile object
    my_car = Automobile(v_type, year, make, model, doors, roof)

    # Step 5: Output the data in the required format
    print("\n--- Vehicle Details ---")
    print(f"Vehicle type: {my_car.vehicle_type}")
    print(f"Year: {my_car.year}")
    print(f"Make: {my_car.make}")
    print(f"Model: {my_car.model}")
    print(f"Number of doors: {my_car.doors}")
    print(f"Type of roof: {my_car.roof}")

if __name__ == "__main__":
    main()