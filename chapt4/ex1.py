def count_sentence_occurrences(file_path, target_sentence):
    count = 0

    with open("C:\Users\asus\Desktop\py\chapt4\text files\file_path", 'r') as file:
        for line in file:
            if target_sentence in line:
                count += 1

    return count

def main():
    file_path = "sen.txt"
    target_sentence = "Hello my name is Chris Ong"

    occurrences = count_sentence_occurrences(file_path, target_sentence)
    print(f"The sentence '{target_sentence}' appears {occurrences} times in the file.")

if __name__ == "__main__":
    main()
