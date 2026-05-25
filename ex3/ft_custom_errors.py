class GardenError(Exception):
    def __init__(self, message="Unknown garden error"):
        Exception().__init__(message) # superler degiscek

class PlantError(GardenError):
    def __init__(self, message="Unknown plant error"):
        GardenError().__init__(message)

class WaterError(GardenError):
    def __init__(self, message="Unknown water error"):
        GardenError().__init__(message)

def plant():
    raise PlantError("The tomato plant is wilting!")

def water():
    raise WaterError("Not enough water in the tank!")

def test_error():
    print(f"=== Custom Garden Errors Demo ===")
    try:
        print(f"Testing PlantError...")
        plant()
    except PlantError as error:
        print(f"Caught PlantError: {error}\n")
    
    try: 
        print(f"Testing WaterError")
        water()
    except WaterError as error:
        print(f"Caught WaterError: {error}\n")
    
    print(f"Testing Catching all garden errors..")
    try:
        plant()
    except GardenError as error:
        print(f"Caught GardenError: {error}")
    try:
        water()
    except GardenError as error:
        print(f"Caught GardenError: {error}\n")
    
    print(f"All custom error types work correctly!")

test_error()




    


