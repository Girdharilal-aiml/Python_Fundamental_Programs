def count_characters():
    s = input("Enter a string: ")
    print(f"Total characters: {len(s)}")
    print(f"Without spaces: {len(s.replace(' ', ''))}")
