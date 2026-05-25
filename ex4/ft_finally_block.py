class GardenError(Exception):
    def __init__(self, message="Unknown garden error"):
        Exception().__init__(message)

class PlantError(GardenError):
    def __init__(self, message="Unknown plant error"):
        GardenError().__init__(message)

class WaterError(GardenError):
    def __init__(self, message="Unknown water error"):
        GardenError().__init__(message)


def water_plant(plant_name):
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    else:
        print(f"Watering {plant_name}: [OK]")

def test_water():
    print("=== Garden Watering System ===\n")
    print("Testing valid plants...")
    try:
        print(f"Opening watering system")
        water_plant("Tomato")
        water_plant("Lettuce")
        water_plant("Carrots")
    except PlantError as error:
        print(f"Caugth PlantError: {error}\n")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system\n")

    print(f"Testing invalid plants..")
    try:
        print(f"Opening watering system")
        water_plant("Tomato")
        water_plant("lettuce")
        water_plant("Carrots")
    except PlantError as error:
        print(f"Caugth PlantError: {error}")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system\n")
    
    print(f"Cleanup always happens, even with errors!")


        
test_water()