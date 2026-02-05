def linear_search():
    lst = [int(x) for x in input("Enter numbers: ").split()]
    target = int(input("Enter number to search: "))
    
    found = False
    for i in range(len(lst)):
        if lst[i] == target:
            print(f"Element found at index {i}")
            found = True
            break
    
    if not found:
        print("Element not found")
