def sum_of_list():
    lst = [int(x) for x in input("Enter numbers: ").split()]
    total = sum(lst)
    print(f"Sum: {total}")