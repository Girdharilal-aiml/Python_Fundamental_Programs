def selection_sort():
    lst = [int(x) for x in input("Enter numbers: ").split()]
    n = len(lst)
    
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    
    print(f"Sorted list: {lst}")
