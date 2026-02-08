def division_error():
    try:
        a = int(input("Enter numerator: "))
        b = int(input("Enter denominator: "))
        result = a / b
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    except ValueError:
        print("Error: Please enter valid numbers!")
