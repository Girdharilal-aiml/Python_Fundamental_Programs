def file_not_found():
    try:
        filename = input("Enter filename: ")
        with open(filename, 'r') as f:
            print(f.read())
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
    except Exception as e:
        print(f"Error: {e}")
