def sum_of_n_numbers():
    n = int(input("Enter N: "))
    total = sum(range(1, n + 1))
    # Or using loop: total = 0; for i in range(1, n+1): total += i
    print(f"Sum of first {n} numbers: {total}")
