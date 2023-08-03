def main():
    # Prompting the user to input a number
    try:
        number = int(input("Enter a number: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    # Checking whether the number is even using the ternary operator
    result = "even" if number % 2 == 0 else "odd"

    # Printing the result
    print(f"The number {number} is {result}.")

if __name__ == "__main__":
    main()
