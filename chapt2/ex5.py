def main():
    locations = ['dubai', 'paris', 'switzerland', 'London', 'amsterdam', 'New York']

    # Print the list and find the length of the list
    print("Original list:", locations)
    print("Length of the list:", len(locations))

    # Use sorted() to print the list in alphabetical order without modifying the actual list
    sorted_list = sorted(locations)
    print("Sorted list in alphabetical order:", sorted_list)

    # Show that the original list is still in its original order
    print("Original list after using sorted():", locations)

    # Use sorted() to print the list in reverse alphabetical order without modifying the actual list
    reverse_sorted_list = sorted(locations, reverse=True)
    print("Sorted list in reverse alphabetical order:", reverse_sorted_list)

    # Show that the original list is still in its original order
    print("Original list after using sorted(reverse=True):", locations)

    # Use reverse() to change the order of the list
    locations.reverse()
    print("List after using reverse():", locations)

    # Use sort() to change the list so it's stored in alphabetical order
    locations.sort()
    print("List after using sort():", locations)

    # Use sort() to change the list so it's stored in reverse alphabetical order
    locations.sort(reverse=True)
    print("List after using sort(reverse=True):", locations)

if __name__ == "__main__":
    main()
