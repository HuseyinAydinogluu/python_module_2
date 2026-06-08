def input_temperature(temp_str: str) -> int:
    temperature = int(temp_str)
    return temperature


def test_temperature() -> None:
    print(" === Garden Temperature ===")

    try:
        print("Input data is '25'")
        result = input_temperature("25")
        print(f"Temperature is now {result}°C\n")
    except Exception:
        print("Invalid temperature input")

    try:
        print("Input data is 'abc'")
        result = input_temperature("abc")
        print(f"Temperature is now {result}°C")
    except Exception:
        print(
            "Caught input_temperature error: invalid literal for "
            "int() with base"
            "10: 'abc'\n"
        )

    print("All tests completed - program didn't crash!")


test_temperature()
