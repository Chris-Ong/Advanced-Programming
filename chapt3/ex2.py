import math

def calculate_square_area(side):
    return side * side

def calculate_circle_area(radius):
    return math.pi * radius * radius

def calculate_triangle_area(base, height):
    return 0.5 * base * height

def main():
    print("Menu:")
    print("1: Calculate the area of a square")
    print("2: Calculate the area of a circle")
    print("3: Calculate the area of a triangle")

    try:
        choice = int(input("Enter your choice (1/2/3): "))
    except ValueError:
        print("Invalid input. Please enter 1, 2, or 3.")
        return

    if choice == 1:
        side = float(input("Enter the side length of the square: "))
        area = calculate_square_area(side)
        print(f"The area of the square is: {area}")
    elif choice == 2:
        radius = float(input("Enter the radius of the circle: "))
        area = calculate_circle_area(radius)
        print(f"The area of the circle is: {area}")
    elif choice == 3:
        base = float(input("Enter the base length of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        area = calculate_triangle_area(base, height)
        print(f"The area of the triangle is: {area}")
    else:
        print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
