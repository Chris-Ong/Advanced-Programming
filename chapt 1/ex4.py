def main():
    # Prompting the user to input two integer numbers
    try:
        num1 = int(input("Enter the first integer number: "))
        num2 = int(input("Enter the second integer number: "))
    except ValueError:
        print("Invalid input. Please enter integers only.")
        return

    # Performing the calculations
    sum_result = num1 + num2
    diff_result = num1 - num2
    product_result = num1 * num2

    # Checking for division by zero to avoid an error
    if num2 != 0:
        quotient_result = num1 / num2
        remainder_result = num1 % num2
    else:
        quotient_result = "Cannot divide by zero"
        remainder_result = "Cannot divide by zero"

    # Printing the results
    print(f"Sum: {sum_result}")
    print(f"Difference: {diff_result}")
    print(f"Product: {product_result}")
    print(f"Quotient: {quotient_result}")
    print(f"Remainder: {remainder_result}")

if __name__ == "__main__":
    main()
