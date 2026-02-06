def word_frequency():
    text = input("Enter text: ")
    words = text.lower().split()
    freq = {}
    
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    
    print("Word frequencies:")
    for word, count in freq.items():
        print(f"{word}: {count}")
