def main():
    count = 0

    while True:
        user_input = input("Do you want to continue? (Y/N): ").strip().upper()
        count += 1

        if user_input != 'Y':
            break

    print(f"The while loop was executed {count} times.")

if __name__ == "__main__":
    main()
