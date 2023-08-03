def calculate_product(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product

def main():
    try:
        num_list = [float(num) for num in input("Enter numbers separated by spaces: ").split()]
    except ValueError:
        print("Invalid input. Please enter valid numbers separated by spaces.")
        return

    if len(num_list) == 0:
        print("List is empty.")
        return

    result = calculate_product(num_list)
    print(f"The product of the list values is: {result}")

if __name__ == "__main__":
    main()
