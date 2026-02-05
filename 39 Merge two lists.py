def merge_two_lists():
    list1 = [int(x) for x in input("Enter first list: ").split()]
    list2 = [int(x) for x in input("Enter second list: ").split()]
    merged = list1 + list2
    print(f"Merged list: {merged}")
