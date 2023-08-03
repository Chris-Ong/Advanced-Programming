def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        raise ValueError("Cannot divide by zero.")
    return num1 / num2

def modulus(num1, num2):
    return num1 % num2

def main():
    print("Calculator Menu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")

    try:
        choice = int(input("Enter your choice (1/2/3/4/5): "))
    except ValueError:
        print("Invalid input. Please enter a valid choice.")
        return

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == 1:
        result = add(num1, num2)
        print(f"The result of addition is: {result}")
    elif choice == 2:
        result = subtract(num1, num2)
        print(f"The result of subtraction is: {result}")
    elif choice == 3:
        result = multiply(num1, num2)
        print(f"The result of multiplication is: {result}")
    elif choice == 4:
        try:
            result = divide(num1, num2)
            print(f"The result of division is: {result}")
        except ValueError as e:
            print(str(e))
    elif choice == 5:
        result = modulus(num1, num2)
        print(f"The result of modulus is: {result}")
    else:
        print("Invalid choice. Please select 1, 2, 3, 4, or 5.")

if __name__ == "__main__":
    main()
