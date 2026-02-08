def library_system():
    books = {}
    
    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == '1':
            book_id = input("Enter book ID: ")
            title = input("Enter title: ")
            author = input("Enter author: ")
            books[book_id] = {"title": title, "author": author, "issued": False}
            print("Book added!")
            
        elif choice == '2':
            for book_id, info in books.items():
                status = "Issued" if info['issued'] else "Available"
                print(f"ID: {book_id}, Title: {info['title']}, Author: {info['author']}, Status: {status}")
                
        elif choice == '3':
            book_id = input("Enter book ID: ")
            if book_id in books:
                info = books[book_id]
                print(f"Title: {info['title']}, Author: {info['author']}")
            else:
                print("Book not found!")
                
        elif choice == '4':
            book_id = input("Enter book ID: ")
            if book_id in books and not books[book_id]['issued']:
                books[book_id]['issued'] = True
                print("Book issued!")
            else:
                print("Book not available!")
                
        elif choice == '5':
            book_id = input("Enter book ID: ")
            if book_id in books and books[book_id]['issued']:
                books[book_id]['issued'] = False
                print("Book returned!")
            else:
                print("Invalid operation!")
                
        elif choice == '6':
            break

