def student_management_system():
    students = {}
    
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Marks")
        print("5. Delete Student")
        print("6. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == '1':
            roll = input("Enter roll number: ")
            name = input("Enter name: ")
            marks = int(input("Enter marks: "))
            students[roll] = {"name": name, "marks": marks}
            print("Student added successfully!")
            
        elif choice == '2':
            if students:
                for roll, info in students.items():
                    print(f"Roll: {roll}, Name: {info['name']}, Marks: {info['marks']}")
            else:
                print("No students found!")
                
        elif choice == '3':
            roll = input("Enter roll number: ")
            if roll in students:
                print(f"Name: {students[roll]['name']}, Marks: {students[roll]['marks']}")
            else:
                print("Student not found!")
                
        elif choice == '4':
            roll = input("Enter roll number: ")
            if roll in students:
                new_marks = int(input("Enter new marks: "))
                students[roll]['marks'] = new_marks
                print("Marks updated!")
            else:
                print("Student not found!")
                
        elif choice == '5':
            roll = input("Enter roll number: ")
            if roll in students:
                del students[roll]
                print("Student deleted!")
            else:
                print("Student not found!")
                
        elif choice == '6':
            print("Exiting...")
            break
