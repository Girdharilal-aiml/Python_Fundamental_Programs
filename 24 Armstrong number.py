def check_armstrong():
    num = int(input("Enter a number: "))
    original = num
    sum_of_cubes = 0
    
    while num > 0:
        digit = num % 10
        sum_of_cubes += digit ** 3
        num //= 10
    
    if original == sum_of_cubes:
        print(f"{original} is an Armstrong number")
    else:
        print(f"{original} is not an Armstrong number")
