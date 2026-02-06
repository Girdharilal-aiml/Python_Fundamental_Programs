def append_file():
    filename = input("Enter filename: ")
    content = input("Enter content to append: ")
    
    with open(filename, 'a') as f:
        f.write(content + "\n")
    print("Content appended successfully!")
