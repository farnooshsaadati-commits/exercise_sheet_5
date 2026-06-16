def copy_element(target, target_idx, source, source_idx):
    """Copy one element from source list into target list."""
    target[target_idx] = source[source_idx]


def merge_sort(arr):
    """
    Sort a list in ascending order using the merge sort algorithm.

    Merge sort works by:
    1. Splitting the list in half
    2. Recursively sorting each half
    3. Merging the two sorted halves back together
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        left_idx = 0
        right_idx = 0
        merged_idx = 0

        while left_idx < len(left) and right_idx < len(right):
            if left[left_idx] <= right[right_idx]:
                copy_element(arr, merged_idx, left, left_idx)
                left_idx += 1
            else:
                copy_element(arr, merged_idx, right, right_idx)
                right_idx += 1
            merged_idx += 1

        while left_idx < len(left):
            arr[merged_idx] = left[left_idx]
            left_idx += 1
            merged_idx += 1

        while right_idx < len(right):
            arr[merged_idx] = right[right_idx]
            right_idx += 1
            merged_idx += 1


import matplotlib.pyplot as plt

my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]

# Plot before sorting
plt.figure(figsize=(8, 4))
plt.bar(range(len(my_list)), my_list, color='steelblue')
plt.title("List Before Sorting")
plt.xlabel("Index")
plt.ylabel("Value")
plt.tight_layout()
plt.show()

merge_sort(my_list)

# Plot after sorting
plt.figure(figsize=(8, 4))
plt.bar(range(len(my_list)), my_list, color='green')
plt.title("List After Sorting")
plt.xlabel("Index")
plt.ylabel("Value")
plt.tight_layout()
plt.show()
