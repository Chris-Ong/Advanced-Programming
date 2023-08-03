class Student:
    def __init__(self, name, mark1, mark2, mark3):
        self.name = name
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3

    def calcGrade(self):
        return (self.mark1 + self.mark2 + self.mark3) / 3

    def display(self):
        print(f"Student Name: {self.name}")
        print(f"Average Grade: {self.calcGrade()}")

def main():
    # Create an object using a constructor with parameters
    student1 = Student("Steve Stevenson", 85, 90, 78)

    # Create an object by taking input from the user
    name = input("Enter student name: ")
    mark1 = int(input("Enter mark1: "))
    mark2 = int(input("Enter mark2: "))
    mark3 = int(input("Enter mark3: "))
    student2 = Student(name, mark1, mark2, mark3)

    # Display the details for both students
    print("\nStudent 1:")
    student1.display()

    print("\nStudent 2:")
    student2.display()

if __name__ == "__main__":
    main()
