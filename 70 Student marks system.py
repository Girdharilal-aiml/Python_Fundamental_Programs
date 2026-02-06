def student_marks_system():
    students = {}
    n = int(input("Enter number of students: "))
    
    for i in range(n):
        name = input(f"Enter student {i+1} name: ")
        marks = int(input(f"Enter marks for {name}: "))
        students[name] = marks
    
    print("\nStudent Records:")
    for name, marks in students.items():
        print(f"{name}: {marks}")
