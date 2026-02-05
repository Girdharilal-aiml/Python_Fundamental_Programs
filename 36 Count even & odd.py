def count_even_odd():
    lst = [int(x) for x in input("Enter numbers: ").split()]
    even_count = sum(1 for x in lst if x % 2 == 0)
    odd_count = len(lst) - even_count
    print(f"Even count: {even_count}, Odd count: {odd_count}")
