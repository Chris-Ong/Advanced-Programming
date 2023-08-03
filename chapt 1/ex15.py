def main():
    numbers = []

    # Requesting five numbers from the user
    for i in range(5):
        try:
            num = float(input(f"Enter number {i+1}: "))
            numbers.append(num)
        except ValueError:
            print("Invalid input. Please enter valid numbers only.")
            return

    # Displaying the list in a nicely formatted way
    print("List of numbers:")
    for num in numbers:
        print(num)

if __name__ == "__main__":
    main()
