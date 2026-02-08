def contact_management():
    contacts = {}
    
    while True:
        print("\n--- Contact Management ---")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            contacts[name] = {"phone": phone, "email": email}
            print("Contact added!")
            
        elif choice == '2':
            for name, info in contacts.items():
                print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")
                
        elif choice == '3':
            name = input("Enter name: ")
            if name in contacts:
                print(f"Phone: {contacts[name]['phone']}, Email: {contacts[name]['email']}")
            else:
                print("Contact not found!")
                
        elif choice == '4':
            name = input("Enter name: ")
            if name in contacts:
                phone = input("Enter new phone: ")
                email = input("Enter new email: ")
                contacts[name] = {"phone": phone, "email": email}
                print("Contact updated!")
            else:
                print("Contact not found!")
                
        elif choice == '5':
            name = input("Enter name: ")
            if name in contacts:
                del contacts[name]
                print("Contact deleted!")
            else:
                print("Contact not found!")
                
        elif choice == '6':
            break
