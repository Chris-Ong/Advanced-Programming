def main():
    try:
        num_days = int(input("Enter the number of days: "))
    except ValueError:
        print("Invalid input. Please enter a valid number of days.")
        return

    # Conversion factors
    seconds_in_minute = 60
    minutes_in_hour = 60
    hours_in_day = 24

    # Calculating the total number of seconds
    total_seconds = num_days * hours_in_day * minutes_in_hour * seconds_in_minute

    # Printing the result
    print(f"There are {total_seconds} seconds in {num_days} days.")

if __name__ == "__main__":
    main()
