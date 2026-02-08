def basic_exception():
    try:
        num = int(input("Enter a number: "))
        print(f"You entered: {num}")
    except ValueError:
        print("Invalid input! Please enter a number.")
