def reverse_list():
    lst = [int(x) for x in input("Enter numbers: ").split()]
    print(f"Original: {lst}")
    print(f"Reversed: {lst[::-1]}")
