def multiple_inputs():
    # Method 1: split and map
    a, b, c = map(int, input("Enter 3 numbers: ").split())
    print(f"Numbers: {a}, {b}, {c}")
    
    # Method 2: list comprehension
    numbers = [int(x) for x in input("Enter numbers: ").split()]
    print(f"List: {numbers}")
