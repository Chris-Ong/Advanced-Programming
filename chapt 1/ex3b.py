def main():
    # Prompting the user to input 3 integer values
    try:
        num1 = int(input("Enter three numbers\nNumber 1: "))
        num2 = int(input("Number 2: "))
        num3 = int(input("Number 3: "))
    except ValueError:
        print("Invalid input. Please enter integers only.")
        return

    # Printing the values in forward order
    print("Your numbers forward:")
    print(num1)
    print(num2)
    print(num3)

    # Printing the values in reversed order
    print("Your numbers reversed:")
    print(num3)
    print(num2)
    print(num1)

if __name__ == "__main__":
    main()