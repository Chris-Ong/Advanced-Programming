def main():
    try:
        num = int(input("Enter a number: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    # Calculate the sum of digits
    sum_of_digits = calculate_sum_of_digits(num)

    # Printing the result
    print(f"The sum of digits in {num} is: {sum_of_digits}")

def calculate_sum_of_digits(number):
    sum_digits = 0
    while number != 0:
        digit = number % 10
        sum_digits += digit
        number //= 10
    return sum_digits

if __name__ == "__main__":
    main()
