def count_digits():
    num = int(input("Enter a number: "))
    count = len(str(abs(num)))
    # Or using loop: count = 0; while num != 0: count += 1; num //= 10
    print(f"Number of digits: {count}")