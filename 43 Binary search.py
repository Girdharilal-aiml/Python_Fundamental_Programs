def binary_search():
    lst = sorted([int(x) for x in input("Enter numbers: ").split()])
    target = int(input("Enter number to search: "))
    
    left, right = 0, len(lst) - 1
    found = False
    
    while left <= right:
        mid = (left + right) // 2
        
        if lst[mid] == target:
            print(f"Element found at index {mid}")
            found = True
            break
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    if not found:
        print("Element not found")
