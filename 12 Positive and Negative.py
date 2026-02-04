def check_positive_negative():
    num = float(input("Enter a number: "))
    if num > 0:
        print(f"{num} is Positive")
    elif num < 0:
        print(f"{num} is Negative")
    else:
        print("Number is Zero")