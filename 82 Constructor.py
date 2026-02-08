class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
    
    def display(self):
        print(f"Name: {self.name}, Roll: {self.roll_no}, Marks: {self.marks}")
