def multiplication_table():
    num = int(input("Enter number: "))
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
