marks = [("CodeLab I", 67),
         ("web Development", 75),
         ("CodeLabII", 74),
         ("Smartphone Apps", 68),
         ("Games Development", 70),
         ("Responsive web", 65)]

# Sort the list of tuples based on marks in ascending order
sorted_low_to_high = sorted(marks, key=lambda x: x[1])

# Sort the list of tuples based on marks in descending order
sorted_high_to_low = sorted(marks, key=lambda x: x[1], reverse=True)

print("Sorted by marks (low to high):")
for subject, mark in sorted_low_to_high:
    print(f"{subject}: {mark}")

print("\nSorted by marks (high to low):")
for subject, mark in sorted_high_to_low:
    print(f"{subject}: {mark}")
