def main():
    # Prompting the user to input the radius of the circle
    try:
        radius = float(input("Enter the radius of the circle: "))
    except ValueError:
        print("Invalid input. Please enter a valid number for the radius.")
        return

    # Constants
    PI = 3.14159

    # Calculating area and circumference
    area = PI * radius * radius
    circumference = 2 * PI * radius

    # Printing the results
    print(f"Area of the circle: {area:.2f}")
    print(f"Circumference of the circle: {circumference:.2f}")

if __name__ == "__main__":
    main()