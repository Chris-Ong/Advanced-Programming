def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)

def main():
    try:
        num = int(input("Enter a non-negative integer to find its factorial: "))
        if num < 0:
            print("Please enter a non-negative integer.")
        else:
            result = factorial_recursive(num)
            print(f"The factorial of {num} is: {result}")
    except ValueError:
        print("Invalid input. Please enter a non-negative integer.")

if __name__ == "__main__":
    main()
