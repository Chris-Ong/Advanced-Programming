def power_recursive(base, exponent):
    if exponent == 0:
        return 1
    elif exponent < 0:
        return 1 / power_recursive(base, -exponent)
    else:
        return base * power_recursive(base, exponent - 1)

def main():
    try:
        base = float(input("Enter the number: "))
        exponent = int(input("Enter the power value: "))
        result = power_recursive(base, exponent)
        print(f"The value of {base} to the power of {exponent} is {result}")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    main()
