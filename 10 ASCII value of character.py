def ascii_value():
    char = input("Enter a character: ")
    if len(char) == 1:
        print(f"ASCII value of '{char}': {ord(char)}")
    else:
        print("Please enter only one character")
