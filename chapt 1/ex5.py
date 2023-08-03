def main():
    # Prompting the user to input the lengths of the three sides
    try:
        side1 = float(input("Enter the length of side 1: "))
        side2 = float(input("Enter the length of side 2: "))
        side3 = float(input("Enter the length of side 3: "))
    except ValueError:
        print("Invalid input. Please enter valid side lengths.")
        return

    # Checking the triangle inequality to determine if it's a valid triangle
    valid_triangle = is_valid_triangle(side1, side2, side3)

    # Printing the result
    if valid_triangle:
        print("It is a valid triangle.")
    else:
        print("It is not a valid triangle.")

def is_valid_triangle(a, b, c):
    # The sum of any two sides of a triangle must be greater than the third side.
    return a + b > c and b + c > a and a + c > b

if __name__ == "__main__":
    main()
