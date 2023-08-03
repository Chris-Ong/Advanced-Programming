def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        print("Cannot divide by zero.")
        return None

def modulus(x, y):
    return x % y

def check_greater(x, y):
    if x > y:
        return x
    elif x < y:
        return y
    else:
        return None

def display_menu():
    print("Calculator Menu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")
    print("6. Check greater number")
    print("7. Exit")

def main():
    while True:
        display_menu()
        choice = int(input("Enter your choice (1-7): "))

        if choice == 7:
            print("Goodbye!")
            break

        if choice < 1 or choice > 6:
            print("Invalid choice. Please try again.")
            continue

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == 1:
            result = add(num1, num2)
        elif choice == 2:
            result = subtract(num1, num2)
        elif choice == 3:
            result = multiply(num1, num2)
        elif choice == 4:
            result = divide(num1, num2)
        elif choice == 5:
            result = modulus(num1, num2)
        elif choice == 6:
            result = check_greater(num1, num2)

        if result is not None:
            print("Result:", result)
        print()

if __name__ == "__main__":
    main()
