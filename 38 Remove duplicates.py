def remove_duplicates():
    lst = [int(x) for x in input("Enter numbers: ").split()]
    unique_list = list(set(lst))
    # To preserve order: unique_list = list(dict.fromkeys(lst))
    print(f"Original: {lst}")
    print(f"After removing duplicates: {unique_list}")
