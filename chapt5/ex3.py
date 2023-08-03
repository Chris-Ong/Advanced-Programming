class Employee:
    def setData(self):
        self.name = input("Enter employee name: ")
        self.age = int(input("Enter employee age: "))
        self.id = input("Enter employee ID: ")
        self.salary = float(input("Enter employee salary: "))

    def getData(self):
        print("Employee Name:", self.name)
        print("Employee Age:", self.age)
        print("Employee ID:", self.id)
        print("Employee Salary:", self.salary)

def main():
    employee_list = []

    for i in range(5):
        employee = Employee()
        print(f"\nEnter details for Employee {i+1}:")
        employee.setData()
        employee_list.append(employee)

    print("\nEmployee Details:")
    for i, employee in enumerate(employee_list, 1):
        print(f"\nEmployee {i}:")
        employee.getData()

if __name__ == "__main__":
    main()
