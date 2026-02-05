"""
PYTHON COMPLETE FOUNDATION PROGRAM SET
========================================
All programs organized by topic with clear examples
"""

# ============================================================================
# 1️⃣ BASIC I/O (Absolute Core)
# ============================================================================

print("="*60)
print("1. BASIC I/O PROGRAMS")
print("="*60)

# 1.1 Print statement
def basic_print():
    print("Hello, World!")
    print("Python", "is", "awesome")
    print(10, 20, 30)

# 1.2 Input from user
def user_input():
    name = input("Enter your name: ")
    print(f"Hello, {name}!")

# 1.3 Type conversion
def type_conversion():
    num_str = "123"
    num_int = int(num_str)
    num_float = float(num_str)
    
    print(f"String: {num_str}, Type: {type(num_str)}")
    print(f"Integer: {num_int}, Type: {type(num_int)}")
    print(f"Float: {num_float}, Type: {type(num_float)}")

# 1.4 Multiple inputs in one line
def multiple_inputs():
    # Method 1: split and map
    a, b, c = map(int, input("Enter 3 numbers: ").split())
    print(f"Numbers: {a}, {b}, {c}")
    
    # Method 2: list comprehension
    numbers = [int(x) for x in input("Enter numbers: ").split()]
    print(f"List: {numbers}")

# 1.5 Formatted output
def formatted_output():
    name = "Python"
    version = 3.11
    
    # f-string
    print(f"Language: {name}, Version: {version:.2f}")
    
    # format method
    print("Language: {}, Version: {:.2f}".format(name, version))
    
    # % formatting
    print("Language: %s, Version: %.2f" % (name, version))


# ============================================================================
# 2️⃣ VARIABLES & EXPRESSIONS
# ============================================================================

print("\n" + "="*60)
print("2. VARIABLES & EXPRESSIONS")
print("="*60)

# 2.1 Swap two numbers
def swap_numbers():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    
    print(f"Before swap: a = {a}, b = {b}")
    
    # Method 1: Using temporary variable
    temp = a
    a = b
    b = temp
    
    # Method 2: Pythonic way
    # a, b = b, a
    
    print(f"After swap: a = {a}, b = {b}")

# 2.2 Simple calculator
def simple_calculator():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operator = input("Enter operator (+, -, *, /): ")
    
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2 if num2 != 0 else "Error: Division by zero"
    else:
        result = "Invalid operator"
    
    print(f"Result: {result}")

# 2.3 Area of circle / rectangle
def area_calculations():
    import math
    
    # Circle
    radius = float(input("Enter radius of circle: "))
    area_circle = math.pi * radius ** 2
    print(f"Area of circle: {area_circle:.2f}")
    
    # Rectangle
    length = float(input("Enter length of rectangle: "))
    width = float(input("Enter width of rectangle: "))
    area_rect = length * width
    print(f"Area of rectangle: {area_rect:.2f}")

# 2.4 Celsius to Fahrenheit
def celsius_to_fahrenheit():
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C = {fahrenheit}°F")

# 2.5 ASCII value of character
def ascii_value():
    char = input("Enter a character: ")
    if len(char) == 1:
        print(f"ASCII value of '{char}': {ord(char)}")
    else:
        print("Please enter only one character")


# ============================================================================
# 3️⃣ CONDITIONAL LOGIC (Decision Making)
# ============================================================================

print("\n" + "="*60)
print("3. CONDITIONAL LOGIC")
print("="*60)

# 3.1 Even / Odd
def check_even_odd():
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")

# 3.2 Positive / Negative
def check_positive_negative():
    num = float(input("Enter a number: "))
    if num > 0:
        print(f"{num} is Positive")
    elif num < 0:
        print(f"{num} is Negative")
    else:
        print("Number is Zero")

# 3.3 Largest of 2 numbers
def largest_of_two():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    
    largest = a if a > b else b
    print(f"Largest: {largest}")

# 3.4 Largest of 3 numbers
def largest_of_three():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    c = float(input("Enter third number: "))
    
    largest = max(a, b, c)
    print(f"Largest: {largest}")

# 3.5 Leap year
def check_leap_year():
    year = int(input("Enter a year: "))
    
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a Leap Year")
    else:
        print(f"{year} is not a Leap Year")

# 3.6 Grade system
def grade_system():
    marks = float(input("Enter marks (0-100): "))
    
    if marks >= 90:
        grade = 'A+'
    elif marks >= 80:
        grade = 'A'
    elif marks >= 70:
        grade = 'B'
    elif marks >= 60:
        grade = 'C'
    elif marks >= 50:
        grade = 'D'
    else:
        grade = 'F'
    
    print(f"Grade: {grade}")

# 3.7 Simple login system
def simple_login():
    correct_username = "admin"
    correct_password = "pass123"
    
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if username == correct_username and password == correct_password:
        print("Login Successful!")
    else:
        print("Invalid credentials!")


# ============================================================================
# 4️⃣ LOOPS (MOST IMPORTANT)
# ============================================================================

print("\n" + "="*60)
print("4. LOOPS PROGRAMS")
print("="*60)

# 4.1 Print numbers 1–N
def print_numbers_1_to_n():
    n = int(input("Enter N: "))
    for i in range(1, n + 1):
        print(i, end=" ")
    print()

# 4.2 Sum of first N numbers
def sum_of_n_numbers():
    n = int(input("Enter N: "))
    total = sum(range(1, n + 1))
    # Or using loop: total = 0; for i in range(1, n+1): total += i
    print(f"Sum of first {n} numbers: {total}")

# 4.3 Multiplication table
def multiplication_table():
    num = int(input("Enter number: "))
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

# 4.4 Count digits
def count_digits():
    num = int(input("Enter a number: "))
    count = len(str(abs(num)))
    # Or using loop: count = 0; while num != 0: count += 1; num //= 10
    print(f"Number of digits: {count}")

# 4.5 Reverse a number
def reverse_number():
    num = int(input("Enter a number: "))
    reversed_num = 0
    original = num
    
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    
    print(f"Reversed number of {original}: {reversed_num}")

# 4.6 Palindrome number
def check_palindrome_number():
    num = int(input("Enter a number: "))
    original = num
    reversed_num = 0
    
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    
    if original == reversed_num:
        print(f"{original} is a Palindrome")
    else:
        print(f"{original} is not a Palindrome")

# 4.7 Armstrong number
def check_armstrong():
    num = int(input("Enter a number: "))
    original = num
    sum_of_cubes = 0
    
    while num > 0:
        digit = num % 10
        sum_of_cubes += digit ** 3
        num //= 10
    
    if original == sum_of_cubes:
        print(f"{original} is an Armstrong number")
    else:
        print(f"{original} is not an Armstrong number")

# 4.8 Prime number
def check_prime():
    num = int(input("Enter a number: "))
    
    if num < 2:
        print(f"{num} is not a Prime number")
        return
    
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(f"{num} is a Prime number")
    else:
        print(f"{num} is not a Prime number")

# 4.9 Factors of a number
def find_factors():
    num = int(input("Enter a number: "))
    print(f"Factors of {num}: ", end="")
    
    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end=" ")
    print()


# ============================================================================
# 5️⃣ PATTERN PROGRAMS (LOGIC POWER)
# ============================================================================

print("\n" + "="*60)
print("5. PATTERN PROGRAMS")
print("="*60)

# 5.1 Star triangle
def star_triangle():
    n = int(input("Enter number of rows: "))
    for i in range(1, n + 1):
        print("* " * i)

# 5.2 Inverted triangle
def inverted_triangle():
    n = int(input("Enter number of rows: "))
    for i in range(n, 0, -1):
        print("* " * i)

# 5.3 Pyramid
def pyramid():
    n = int(input("Enter number of rows: "))
    for i in range(1, n + 1):
        print(" " * (n - i) + "* " * i)

# 5.4 Number triangle
def number_triangle():
    n = int(input("Enter number of rows: "))
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

# 5.5 Floyd's triangle
def floyds_triangle():
    n = int(input("Enter number of rows: "))
    num = 1
    for i in range(1, n + 1):
        for j in range(i):
            print(num, end=" ")
            num += 1
        print()

# 5.6 Diamond pattern
def diamond_pattern():
    n = int(input("Enter number of rows: "))
    
    # Upper half
    for i in range(1, n + 1):
        print(" " * (n - i) + "* " * i)
    
    # Lower half
    for i in range(n - 1, 0, -1):
        print(" " * (n - i) + "* " * i)


# ============================================================================
# 6️⃣ LIST / ARRAY PROGRAMS (CORE)
# ============================================================================

print("\n" + "="*60)
print("6. LIST/ARRAY PROGRAMS")
print("="*60)

# 6.1 Create list dynamically
def create_list_dynamically():
    n = int(input("Enter number of elements: "))
    lst = []
    for i in range(n):
        element = int(input(f"Enter element {i+1}: "))
        lst.append(element)
    print(f"List: {lst}")

# 6.2 Sum of list
def sum_of_list():
    lst = [int(x) for x in input("Enter numbers: ").split()]
    total = sum(lst)
    print(f"Sum: {total}")

# 6.3 Max / Min in list
def max_min_in_list():
    lst = [int(x) for x in input("Enter numbers: ").split()]
    print(f"Maximum: {max(lst)}")
    print(f"Minimum: {min(lst)}")

# 6.4 Count even & odd
def count_even_odd():
    lst = [int(x) for x in input("Enter numbers: ").split()]
    even_count = sum(1 for x in lst if x % 2 == 0)
    odd_count = len(lst) - even_count
    print(f"Even count: {even_count}, Odd count: {odd_count}")

# 6.5 Reverse list
def reverse_list():
    lst = [int(x) for x in input("Enter numbers: ").split()]
    print(f"Original: {lst}")
    print(f"Reversed: {lst[::-1]}")

# 6.6 Remove duplicates
def remove_duplicates():
    lst = [int(x) for x in input("Enter numbers: ").split()]
    unique_list = list(set(lst))
    # To preserve order: unique_list = list(dict.fromkeys(lst))
    print(f"Original: {lst}")
    print(f"After removing duplicates: {unique_list}")

# 6.7 Merge two lists
def merge_two_lists():
    list1 = [int(x) for x in input("Enter first list: ").split()]
    list2 = [int(x) for x in input("Enter second list: ").split()]
    merged = list1 + list2
    print(f"Merged list: {merged}")

# 6.8 Rotate list
def rotate_list():
    lst = [int(x) for x in input("Enter numbers: ").split()]
    k = int(input("Enter positions to rotate: "))
    k = k % len(lst)
    rotated = lst[k:] + lst[:k]
    print(f"Original: {lst}")
    print(f"Rotated by {k}: {rotated}")

# 6.9 Second largest element
def second_largest():
    lst = [int(x) for x in input("Enter numbers: ").split()]
    unique_sorted = sorted(set(lst), reverse=True)
    if len(unique_sorted) >= 2:
        print(f"Second largest: {unique_sorted[1]}")
    else:
        print("Not enough unique elements")


# ============================================================================
# 7️⃣ SEARCHING ALGORITHMS
# ============================================================================

print("\n" + "="*60)
print("7. SEARCHING ALGORITHMS")
print("="*60)

# 7.1 Linear search
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

# 7.2 Binary search
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


# ============================================================================
# 8️⃣ SORTING ALGORITHMS 🔥🔥🔥
# ============================================================================

print("\n" + "="*60)
print("8. SORTING ALGORITHMS")
print("="*60)

# 8.1 Bubble sort
def bubble_sort():
    lst = [int(x) for x in input("Enter numbers: ").split()]
    n = len(lst)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    
    print(f"Sorted list: {lst}")

# 8.2 Selection sort
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

# 8.3 Insertion sort
def insertion_sort():
    lst = [int(x) for x in input("Enter numbers: ").split()]
    
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    
    print(f"Sorted list: {lst}")

# 8.4 Quick sort
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

# 8.5 Merge sort
def merge_sort_demo():
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        
        return merge(left, right)
    
    def merge(left, right):
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    
    lst = [int(x) for x in input("Enter numbers: ").split()]
    sorted_lst = merge_sort(lst)
    print(f"Sorted list: {sorted_lst}")


# ============================================================================
# 9️⃣ STRING PROGRAMS (VERY IMPORTANT)
# ============================================================================

print("\n" + "="*60)
print("9. STRING PROGRAMS")
print("="*60)

# 9.1 Reverse string
def reverse_string():
    s = input("Enter a string: ")
    print(f"Reversed: {s[::-1]}")

# 9.2 Palindrome string
def check_palindrome_string():
    s = input("Enter a string: ").lower().replace(" ", "")
    if s == s[::-1]:
        print(f"'{s}' is a Palindrome")
    else:
        print(f"'{s}' is not a Palindrome")

# 9.3 Count vowels
def count_vowels():
    s = input("Enter a string: ").lower()
    vowels = "aeiou"
    count = sum(1 for char in s if char in vowels)
    print(f"Number of vowels: {count}")

# 9.4 Count words
def count_words():
    s = input("Enter a string: ")
    words = s.split()
    print(f"Number of words: {len(words)}")

# 9.5 Count characters
def count_characters():
    s = input("Enter a string: ")
    print(f"Total characters: {len(s)}")
    print(f"Without spaces: {len(s.replace(' ', ''))}")

# 9.6 Remove spaces
def remove_spaces():
    s = input("Enter a string: ")
    print(f"Without spaces: {s.replace(' ', '')}")

# 9.7 Replace characters
def replace_characters():
    s = input("Enter a string: ")
    old_char = input("Character to replace: ")
    new_char = input("Replace with: ")
    print(f"Result: {s.replace(old_char, new_char)}")

# 9.8 Frequency of characters
def character_frequency():
    s = input("Enter a string: ")
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    
    print("Character frequencies:")
    for char, count in sorted(freq.items()):
        print(f"'{char}': {count}")

# 9.9 Anagram check
def check_anagram():
    s1 = input("Enter first string: ").lower().replace(" ", "")
    s2 = input("Enter second string: ").lower().replace(" ", "")
    
    if sorted(s1) == sorted(s2):
        print("Strings are Anagrams")
    else:
        print("Strings are not Anagrams")

# 9.10 Longest word
def find_longest_word():
    s = input("Enter a sentence: ")
    words = s.split()
    longest = max(words, key=len)
    print(f"Longest word: '{longest}' (length: {len(longest)})")


# ============================================================================
# 🔟 FUNCTIONS (REUSABILITY)
# ============================================================================

print("\n" + "="*60)
print("10. FUNCTIONS")
print("="*60)

# 10.1 Function with parameters
def greet(name, age):
    print(f"Hello {name}, you are {age} years old!")

# 10.2 Function with return
def add_numbers(a, b):
    return a + b

# 10.3 Default arguments
def power(base, exponent=2):
    return base ** exponent

# 10.4 Recursive function
def countdown(n):
    if n <= 0:
        print("Done!")
    else:
        print(n)
        countdown(n - 1)

# 10.5 Factorial using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


# ============================================================================
# 1️⃣1️⃣ TUPLES & SETS
# ============================================================================

print("\n" + "="*60)
print("11. TUPLES & SETS")
print("="*60)

# 11.1 Tuple operations
def tuple_operations():
    t = (1, 2, 3, 4, 5)
    print(f"Tuple: {t}")
    print(f"Length: {len(t)}")
    print(f"Max: {max(t)}, Min: {min(t)}")
    print(f"Index of 3: {t.index(3)}")

# 11.2 Convert tuple to list
def tuple_to_list():
    t = (1, 2, 3, 4, 5)
    lst = list(t)
    print(f"Tuple: {t}")
    print(f"List: {lst}")

# 11.3 Set operations
def set_operations():
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    
    print(f"Set 1: {set1}")
    print(f"Set 2: {set2}")
    print(f"Union: {set1 | set2}")
    print(f"Intersection: {set1 & set2}")
    print(f"Difference: {set1 - set2}")

# 11.4 Remove duplicates using set
def remove_duplicates_set():
    lst = [1, 2, 2, 3, 4, 4, 5, 5, 5]
    unique = list(set(lst))
    print(f"Original: {lst}")
    print(f"Unique: {unique}")


# ============================================================================
# 1️⃣2️⃣ DICTIONARY PROGRAMS
# ============================================================================

print("\n" + "="*60)
print("12. DICTIONARY PROGRAMS")
print("="*60)

# 12.1 Create dictionary
def create_dictionary():
    student = {
        "name": "John",
        "age": 20,
        "grade": "A"
    }
    print(student)
    print(f"Name: {student['name']}")

# 12.2 Word frequency
def word_frequency():
    text = input("Enter text: ")
    words = text.lower().split()
    freq = {}
    
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    
    print("Word frequencies:")
    for word, count in freq.items():
        print(f"{word}: {count}")

# 12.3 Student marks system
def student_marks_system():
    students = {}
    n = int(input("Enter number of students: "))
    
    for i in range(n):
        name = input(f"Enter student {i+1} name: ")
        marks = int(input(f"Enter marks for {name}: "))
        students[name] = marks
    
    print("\nStudent Records:")
    for name, marks in students.items():
        print(f"{name}: {marks}")

# 12.4 Phone book
def phone_book():
    contacts = {}
    
    while True:
        print("\n1. Add Contact")
        print("2. Search Contact")
        print("3. Display All")
        print("4. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            contacts[name] = phone
        elif choice == '2':
            name = input("Enter name to search: ")
            print(f"Phone: {contacts.get(name, 'Not found')}")
        elif choice == '3':
            for name, phone in contacts.items():
                print(f"{name}: {phone}")
        elif choice == '4':
            break

# 12.5 Sorting dictionary by value
def sort_dict_by_value():
    d = {'apple': 3, 'banana': 1, 'cherry': 2}
    sorted_d = dict(sorted(d.items(), key=lambda x: x[1]))
    print(f"Original: {d}")
    print(f"Sorted by value: {sorted_d}")


# ============================================================================
# 1️⃣3️⃣ FILE HANDLING (REAL PROGRAMS)
# ============================================================================

print("\n" + "="*60)
print("13. FILE HANDLING")
print("="*60)

# 13.1 Read file
def read_file():
    try:
        filename = input("Enter filename: ")
        with open(filename, 'r') as f:
            content = f.read()
            print(content)
    except FileNotFoundError:
        print("File not found!")

# 13.2 Write file
def write_file():
    filename = input("Enter filename: ")
    content = input("Enter content to write: ")
    
    with open(filename, 'w') as f:
        f.write(content)
    print("File written successfully!")

# 13.3 Append file
def append_file():
    filename = input("Enter filename: ")
    content = input("Enter content to append: ")
    
    with open(filename, 'a') as f:
        f.write(content + "\n")
    print("Content appended successfully!")

# 13.4 Count lines / words
def count_lines_words():
    try:
        filename = input("Enter filename: ")
        with open(filename, 'r') as f:
            lines = f.readlines()
            word_count = sum(len(line.split()) for line in lines)
            
        print(f"Lines: {len(lines)}")
        print(f"Words: {word_count}")
    except FileNotFoundError:
        print("File not found!")

# 13.5 Copy file
def copy_file():
    try:
        source = input("Enter source filename: ")
        dest = input("Enter destination filename: ")
        
        with open(source, 'r') as src:
            content = src.read()
        
        with open(dest, 'w') as dst:
            dst.write(content)
        
        print("File copied successfully!")
    except FileNotFoundError:
        print("Source file not found!")


# ============================================================================
# 1️⃣4️⃣ EXCEPTION HANDLING
# ============================================================================

print("\n" + "="*60)
print("14. EXCEPTION HANDLING")
print("="*60)

# 14.1 Try–except
def basic_exception():
    try:
        num = int(input("Enter a number: "))
        print(f"You entered: {num}")
    except ValueError:
        print("Invalid input! Please enter a number.")

# 14.2 Division error handling
def division_error():
    try:
        a = int(input("Enter numerator: "))
        b = int(input("Enter denominator: "))
        result = a / b
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    except ValueError:
        print("Error: Please enter valid numbers!")

# 14.3 File not found handling
def file_not_found():
    try:
        filename = input("Enter filename: ")
        with open(filename, 'r') as f:
            print(f.read())
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
    except Exception as e:
        print(f"Error: {e}")


# ============================================================================
# 1️⃣5️⃣ OOP (OBJECT-ORIENTED) 🔥
# ============================================================================

print("\n" + "="*60)
print("15. OBJECT-ORIENTED PROGRAMMING")
print("="*60)

# 15.1 Class & object
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# 15.2 Constructor
class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
    
    def display(self):
        print(f"Name: {self.name}, Roll: {self.roll_no}, Marks: {self.marks}")

# 15.3 Encapsulation
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private variable
    
    def deposit(self, amount):
        self.__balance += amount
    
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance!")
    
    def get_balance(self):
        return self.__balance

# 15.4 Inheritance
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# 15.5 Polymorphism
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2

# 15.6 Method overriding
class Parent:
    def show(self):
        print("Parent class method")

class Child(Parent):
    def show(self):
        print("Child class method")


# ============================================================================
# 1️⃣6️⃣ MODULES & PACKAGES
# ============================================================================

print("\n" + "="*60)
print("16. MODULES & PACKAGES")
print("="*60)

# 16.1 Import math module
def use_math_module():
    import math
    
    print(f"Pi: {math.pi}")
    print(f"Square root of 16: {math.sqrt(16)}")
    print(f"Sin(90): {math.sin(math.radians(90))}")

# 16.2 Create own module (would be in separate file)
# mymodule.py would contain:
"""
def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b
"""

# 16.3 Use random module
def use_random_module():
    import random
    
    print(f"Random number: {random.randint(1, 100)}")
    print(f"Random choice: {random.choice(['apple', 'banana', 'cherry'])}")
    
    lst = [1, 2, 3, 4, 5]
    random.shuffle(lst)
    print(f"Shuffled list: {lst}")


# ============================================================================
# 1️⃣7️⃣ MINI PROJECTS (BIG-PROGRAM THINKING)
# ============================================================================

print("\n" + "="*60)
print("17. MINI PROJECTS")
print("="*60)

# 17.1 Number guessing game
def number_guessing_game():
    import random
    
    number = random.randint(1, 100)
    attempts = 0
    
    print("Guess the number between 1 and 100!")
    
    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1
        
        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed it in {attempts} attempts!")
            break

# 17.2 Student management system
def student_management_system():
    students = {}
    
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Marks")
        print("5. Delete Student")
        print("6. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == '1':
            roll = input("Enter roll number: ")
            name = input("Enter name: ")
            marks = int(input("Enter marks: "))
            students[roll] = {"name": name, "marks": marks}
            print("Student added successfully!")
            
        elif choice == '2':
            if students:
                for roll, info in students.items():
                    print(f"Roll: {roll}, Name: {info['name']}, Marks: {info['marks']}")
            else:
                print("No students found!")
                
        elif choice == '3':
            roll = input("Enter roll number: ")
            if roll in students:
                print(f"Name: {students[roll]['name']}, Marks: {students[roll]['marks']}")
            else:
                print("Student not found!")
                
        elif choice == '4':
            roll = input("Enter roll number: ")
            if roll in students:
                new_marks = int(input("Enter new marks: "))
                students[roll]['marks'] = new_marks
                print("Marks updated!")
            else:
                print("Student not found!")
                
        elif choice == '5':
            roll = input("Enter roll number: ")
            if roll in students:
                del students[roll]
                print("Student deleted!")
            else:
                print("Student not found!")
                
        elif choice == '6':
            print("Exiting...")
            break

# 17.3 ATM system
def atm_system():
    balance = 1000
    pin = "1234"
    
    entered_pin = input("Enter PIN: ")
    
    if entered_pin != pin:
        print("Invalid PIN!")
        return
    
    while True:
        print("\n--- ATM Menu ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == '1':
            print(f"Balance: ${balance}")
            
        elif choice == '2':
            amount = float(input("Enter amount to deposit: "))
            balance += amount
            print(f"Deposited ${amount}. New balance: ${balance}")
            
        elif choice == '3':
            amount = float(input("Enter amount to withdraw: "))
            if amount <= balance:
                balance -= amount
                print(f"Withdrawn ${amount}. New balance: ${balance}")
            else:
                print("Insufficient balance!")
                
        elif choice == '4':
            print("Thank you!")
            break

# 17.4 Library system
def library_system():
    books = {}
    
    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == '1':
            book_id = input("Enter book ID: ")
            title = input("Enter title: ")
            author = input("Enter author: ")
            books[book_id] = {"title": title, "author": author, "issued": False}
            print("Book added!")
            
        elif choice == '2':
            for book_id, info in books.items():
                status = "Issued" if info['issued'] else "Available"
                print(f"ID: {book_id}, Title: {info['title']}, Author: {info['author']}, Status: {status}")
                
        elif choice == '3':
            book_id = input("Enter book ID: ")
            if book_id in books:
                info = books[book_id]
                print(f"Title: {info['title']}, Author: {info['author']}")
            else:
                print("Book not found!")
                
        elif choice == '4':
            book_id = input("Enter book ID: ")
            if book_id in books and not books[book_id]['issued']:
                books[book_id]['issued'] = True
                print("Book issued!")
            else:
                print("Book not available!")
                
        elif choice == '5':
            book_id = input("Enter book ID: ")
            if book_id in books and books[book_id]['issued']:
                books[book_id]['issued'] = False
                print("Book returned!")
            else:
                print("Invalid operation!")
                
        elif choice == '6':
            break

# 17.5 Quiz system
def quiz_system():
    questions = [
        {"q": "What is the capital of France?", "a": "Paris"},
        {"q": "What is 2 + 2?", "a": "4"},
        {"q": "What is the largest planet?", "a": "Jupiter"}
    ]
    
    score = 0
    
    print("--- Quiz Time! ---")
    for i, item in enumerate(questions, 1):
        print(f"\nQ{i}: {item['q']}")
        answer = input("Your answer: ")
        
        if answer.lower() == item['a'].lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! Correct answer: {item['a']}")
    
    print(f"\nYour score: {score}/{len(questions)}")

# 17.6 To-Do list
def todo_list():
    tasks = []
    
    while True:
        print("\n--- To-Do List ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Complete")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == '1':
            task = input("Enter task: ")
            tasks.append({"task": task, "completed": False})
            print("Task added!")
            
        elif choice == '2':
            for i, task in enumerate(tasks, 1):
                status = "✓" if task['completed'] else "✗"
                print(f"{i}. [{status}] {task['task']}")
                
        elif choice == '3':
            idx = int(input("Enter task number: ")) - 1
            if 0 <= idx < len(tasks):
                tasks[idx]['completed'] = True
                print("Task marked complete!")
            else:
                print("Invalid task number!")
                
        elif choice == '4':
            idx = int(input("Enter task number: ")) - 1
            if 0 <= idx < len(tasks):
                tasks.pop(idx)
                print("Task deleted!")
            else:
                print("Invalid task number!")
                
        elif choice == '5':
            break

# 17.7 Contact management system
def contact_management():
    contacts = {}
    
    while True:
        print("\n--- Contact Management ---")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            contacts[name] = {"phone": phone, "email": email}
            print("Contact added!")
            
        elif choice == '2':
            for name, info in contacts.items():
                print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")
                
        elif choice == '3':
            name = input("Enter name: ")
            if name in contacts:
                print(f"Phone: {contacts[name]['phone']}, Email: {contacts[name]['email']}")
            else:
                print("Contact not found!")
                
        elif choice == '4':
            name = input("Enter name: ")
            if name in contacts:
                phone = input("Enter new phone: ")
                email = input("Enter new email: ")
                contacts[name] = {"phone": phone, "email": email}
                print("Contact updated!")
            else:
                print("Contact not found!")
                
        elif choice == '5':
            name = input("Enter name: ")
            if name in contacts:
                del contacts[name]
                print("Contact deleted!")
            else:
                print("Contact not found!")
                
        elif choice == '6':
            break


# ============================================================================
# MAIN MENU TO RUN ALL PROGRAMS
# ============================================================================

def main():
    print("\n" + "="*60)
    print("PYTHON COMPLETE FOUNDATION PROGRAM SET")
    print("="*60)
    print("This file contains ALL programs from the foundation set.")
    print("You can run individual functions or modify them as needed.")
    print("="*60)
    
    # Example usage:
    # Uncomment any function to run it
    
    # basic_print()
    # swap_numbers()
    # check_even_odd()
    # print_numbers_1_to_n()
    # star_triangle()
    # linear_search()
    # bubble_sort()
    # reverse_string()
    # greet("Alice", 25)
    # print(factorial(5))
    # number_guessing_game()
    
    print("\nAll programs are ready to use!")
    print("Read through the code and run any function you need.")

if __name__ == "__main__":
    main()