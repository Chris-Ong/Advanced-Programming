def write_bio_to_file(file_path):
    with open(file_path, 'w') as file:
        name = input("Enter your Name: ")
        age = input("Enter your Age: ")
        hometown = input("Enter your Hometown: ")

        file.write(f"{name}\n")
        file.write(f"{age}\n")
        file.write(f"{hometown}\n")

def read_bio_from_file(file_path):
    with open(file_path, 'r') as file:
        name = file.readline().strip()
        age = file.readline().strip()
        hometown = file.readline().strip()

        print("Name:", name)
        print("Age:", age)
        print("Hometown:", hometown)

def main():
    file_path = "bio.txt"

    write_bio_to_file(file_path)
    print("Information written to the file successfully!")

    print("\nReading the information from the file:")
    read_bio_from_file(file_path)

if __name__ == "__main__":
    main()
