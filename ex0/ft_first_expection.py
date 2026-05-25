def input_temperature(temp_str):
    temperature = int(temp_str)
    return temperature

def test_temperature():
    print(f" === Garden Temperature ===")

    try:
        print(f"Input data is '25'")
        result = input_temperature("25")
        print(f"Temperature is now {result}°C\n")
    except:
        print("Invalid temperature input")

    try:
        print(f"Input data is 'abc'")
        result = input_temperature("abc")
        print(f"Temperature is now {result}°C")
    except:
        print(f"Caught input_temperature error: invalid literal for int() with base 10: 'abc'\n")

    print(f"All tests completed - program didn't crash!")


test_temperature()

