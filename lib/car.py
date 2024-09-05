class Car:
    def __init__(self, engine):
        self.engine = engine

class Engine:
    def __init__(self, cylinders, fuelType):
        self.cylinders = cylinders
        self.fuelType = fuelType

# Create an Engine instance
engine = Engine(cylinders=4, fuelType="Gasoline")

# Create a Car instance with the Engine
car = Car(engine)

# Output the attributes of the Car and its Engine
print(f"Car Engine Details:")
print(f" - Cylinders: {car.engine.cylinders}")
print(f" - Fuel Type: {car.engine.fuelType}")      


four_cylinder_engine = Engine(4, 'regular')
acura_tlx = Car(four_cylinder_engine)

print("Car Engine Details:")
print(f" - Cylinders: {acura_tlx.engine.cylinders}")
print(f" - Fuel Type: {acura_tlx.engine.fuelType}")    
