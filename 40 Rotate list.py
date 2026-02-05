def rotate_list():
    lst = [int(x) for x in input("Enter numbers: ").split()]
    k = int(input("Enter positions to rotate: "))
    k = k % len(lst)
    rotated = lst[k:] + lst[:k]
    print(f"Original: {lst}")
    print(f"Rotated by {k}: {rotated}")
