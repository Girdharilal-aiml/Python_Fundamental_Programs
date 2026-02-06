def read_file():
    try:
        filename = input("Enter filename: ")
        with open(filename, 'r') as f:
            content = f.read()
            print(content)
    except FileNotFoundError:
        print("File not found!")
