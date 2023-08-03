import numpy as np

def main():
    a = np.array([20, 23, 82, 40, 32, 15, 67, 52])

    # Find the indices of even numbers
    even_indices = np.where(a % 2 == 0)[0]
    print("Indices of even numbers:", even_indices)

    # Sort the array
    sorted_array = np.sort(a)
    print("Sorted array:", sorted_array)

    # Slice elements from index 3 to the end of the array
    slice1 = a[3:]
    print("Slice from index 3 to the end:", slice1)

    # Slice elements from index 0 to index 4
    slice2 = a[0:5]
    print("Slice from index 0 to index 4:", slice2)

    # Print [32 15 67] using negative slicing
    negative_slice = a[-5:-2]
    print("Negative slice [32 15 67]:", negative_slice)

if __name__ == "__main__":
    main()
