def power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent == 1:
        return base
    else:
        return base * power(base, exponent - 1)

def main():
    try:
        base = float(input("Enter the base number: "))
        exponent = int(input("Enter the power value: "))

        result = power(base, exponent)
        print(f"The value of {base} to the power of {exponent} is {result}.")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    main()
