def diamond_pattern():
    n = int(input("Enter number of rows: "))
    
    # Upper half
    for i in range(1, n + 1):
        print(" " * (n - i) + "* " * i)
    
    # Lower half
    for i in range(n - 1, 0, -1):
        print(" " * (n - i) + "* " * i)