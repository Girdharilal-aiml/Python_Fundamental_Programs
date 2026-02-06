def copy_file():
    try:
        source = input("Enter source filename: ")
        dest = input("Enter destination filename: ")
        
        with open(source, 'r') as src:
            content = src.read()
        
        with open(dest, 'w') as dst:
            dst.write(content)
        
        print("File copied successfully!")
    except FileNotFoundError:
        print("Source file not found!")
