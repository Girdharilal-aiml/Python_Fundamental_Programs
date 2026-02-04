def largest_of_two():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    
    largest = a if a > b else b
    print(f"Largest: {largest}")
