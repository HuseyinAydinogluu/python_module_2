class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        Exception.__init__(self, message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        GardenError.__init__(self, message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        GardenError.__init__(self, message)


def plant() -> None:
    raise PlantError("The tomato plant is wilting!")


def water() -> None:
    raise WaterError("Not enough water in the tank!")


def test_error() -> None:
    print("=== Custom Garden Errors Demo ===")
    try:
        print("Testing PlantError...")
        plant()
    except PlantError as error:
        print(f"Caught PlantError: {error}\n")

    try:
        print("Testing WaterError")
        water()
    except WaterError as error:
        print(f"Caught WaterError: {error}\n")

    print("Testing Catching all garden errors..")
    try:
        plant()
    except GardenError as error:
        print(f"Caught GardenError: {error}")
    try:
        water()
    except GardenError as error:
        print(f"Caught GardenError: {error}\n")

    print("All custom error types work correctly!")


test_error()
