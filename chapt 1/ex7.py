def main():
    # Prompting the user to input three numbers
    try:
        num1 = float(input("Enter number 1: "))
        num2 = float(input("Enter number 2: "))
        num3 = float(input("Enter number 3: "))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return

    # Using ternary operator to find the largest number
    largest = num1 if num1 >= num2 and num1 >= num3 else (num2 if num2 >= num3 else num3)

    # Printing the largest number
    print(f"The largest number is: {largest}")

if __name__ == "__main__":
    main()