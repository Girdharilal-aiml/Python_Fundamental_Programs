def floyds_triangle():
    n = int(input("Enter number of rows: "))
    num = 1
    for i in range(1, n + 1):
        for j in range(i):
            print(num, end=" ")
            num += 1
        print()