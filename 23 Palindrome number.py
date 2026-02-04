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
