def quick_sort_demo():
    def quick_sort(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)
    
    lst = [int(x) for x in input("Enter numbers: ").split()]
    sorted_lst = quick_sort(lst)
    print(f"Sorted list: {sorted_lst}")
