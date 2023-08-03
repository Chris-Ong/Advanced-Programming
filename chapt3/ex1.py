def main():
    try:
        num1 = float(input("Enter the first value: "))
        num2 = float(input("Enter the second value: "))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return

    # Calculate the sum of the two values
    result = num1 + num2

    # Output the result to the screen
    print(f"The sum of {num1} and {num2} is: {result}")

if __name__ == "__main__":
    main()
