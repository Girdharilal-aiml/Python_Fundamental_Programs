def second_largest():
    lst = [int(x) for x in input("Enter numbers: ").split()]
    unique_sorted = sorted(set(lst), reverse=True)
    if len(unique_sorted) >= 2:
        print(f"Second largest: {unique_sorted[1]}")
    else:
        print("Not enough unique elements")

