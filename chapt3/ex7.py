def count_letters(word):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    special_chars = " !@#$%^&*()-_=+[{]};:'\",<.>/?\\|"

    letter_count = 0
    vowel_count = 0
    consonant_count = 0
    special_char_count = 0

    for char in word:
        if char.isalpha():
            letter_count += 1
            if char in vowels:
                vowel_count += 1
            elif char in consonants:
                consonant_count += 1
        elif char in special_chars:
            special_char_count += 1

    return letter_count, vowel_count, consonant_count, special_char_count

def main():
    word = input("Enter a word: ")

    letter_count, vowel_count, consonant_count, special_char_count = count_letters(word)

    print("Total number of letters:", letter_count)
    print("Number of vowels:", vowel_count)
    print("Number of consonants:", consonant_count)
    print("Number of special characters:", special_char_count)

if __name__ == "__main__":
    main()
