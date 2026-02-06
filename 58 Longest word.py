def find_longest_word():
    s = input("Enter a sentence: ")
    words = s.split()
    longest = max(words, key=len)
    print(f"Longest word: '{longest}' (length: {len(longest)})")

