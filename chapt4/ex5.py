def calculate_product(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product

def main():
    try:
        numbers = []
        n = int(input("Enter the number of elements in the list: "))
        for i in range(n):
            num = float(input(f"Enter element {i + 1}: "))
            numbers.append(num)

        result = calculate_product(numbers)
        print(f"The product of the elements in the list is: {result}")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    main()
