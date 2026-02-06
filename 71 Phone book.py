def phone_book():
    contacts = {}
    
    while True:
        print("\n1. Add Contact")
        print("2. Search Contact")
        print("3. Display All")
        print("4. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            contacts[name] = phone
        elif choice == '2':
            name = input("Enter name to search: ")
            print(f"Phone: {contacts.get(name, 'Not found')}")
        elif choice == '3':
            for name, phone in contacts.items():
                print(f"{name}: {phone}")
        elif choice == '4':
            break
