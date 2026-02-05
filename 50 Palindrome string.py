def check_palindrome_string():
    s = input("Enter a string: ").lower().replace(" ", "")
    if s == s[::-1]:
        print(f"'{s}' is a Palindrome")
    else:
        print(f"'{s}' is not a Palindrome")
