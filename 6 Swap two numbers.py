def swap_numbers():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    
    print(f"Before swap: a = {a}, b = {b}")
    
    # Method 1: Using temporary variable
    temp = a
    a = b
    b = temp
    
    # Method 2: Pythonic way
    # a, b = b, a
    
    print(f"After swap: a = {a}, b = {b}")
