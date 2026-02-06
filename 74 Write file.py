def write_file():
    filename = input("Enter filename: ")
    content = input("Enter content to write: ")
    
    with open(filename, 'w') as f:
        f.write(content)
    print("File written successfully!")
