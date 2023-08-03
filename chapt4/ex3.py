def read_numbers_from_file(file_path):
    numbers = []
    with open("c:\Users\asus\Desktop\py\chapt4\text files\file_path", 'r') as file:
        for line in file:
            numbers.append(int(line.strip()))
    return numbers

def main():
    file_path = "numbers.txt"
    numbers_list = read_numbers_from_file(file_path)

    print("Numbers in integer format:")
    for number in numbers_list:
        print(number)

if __name__ == "__main__":
    main()
