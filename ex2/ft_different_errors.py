def garden_operations(operation_number):

    if operation_number == 0:

        int("abc")

    elif operation_number == 1:

        result = 10 / 0

    elif operation_number == 2:

        open("/non/existent/file")

    elif operation_number == 3:

        result = "flower" + 5

    else:
        return


def test_error_types():

    print("=== Garden Error Types Demo ===")

    for i in range(5):

        print(f"Testing operation {i}...")

        try:
            garden_operations(i)

            print("Operation completed successfully")

        except ValueError as error:
            print(f"Caught ValueError: {error}")

        except ZeroDivisionError as error:
            print(f"Caught ZeroDivisionError: {error}")

        except FileNotFoundError as error:
            print(f"Caught FileNotFoundError: {error}")

        except TypeError as error:
            print(f"Caught TypeError: {error}")

    print("\n=== Multiple Error Catch Demo ===")

    try:
        garden_operations(0)
        garden_operations(3)

    except (ValueError, TypeError) as error:
        print(f"Caught multiple possible errors: {error}")

    print("\nAll error types tested successfully!")

"1  "
test_error_types()