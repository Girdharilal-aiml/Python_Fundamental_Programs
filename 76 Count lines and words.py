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
