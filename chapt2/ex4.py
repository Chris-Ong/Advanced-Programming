def main():
    students = ["Adam", "Aether", "", "Bella", "Barry","Chris","Calvin", "Eric","Elmo","Drake"]

    # Count the number of times each item appears in the list
    item_count = {}
    for item in students:
        if item in item_count:
            item_count[item] += 1
        else:
            item_count[item] = 1

    # Display the result
    for item, count in item_count.items():
        print(f"{item}: {count}")

if __name__ == "__main__":
    main()
