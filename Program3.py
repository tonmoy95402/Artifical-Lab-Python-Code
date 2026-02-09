def binary_search_with_bubble_sort(arr, target):
    n = len(arr)

    # Bubble Sort
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    # Binary Search
    left = 0
    right = n - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# Main program
n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    arr.append(int(input(f"Enter element {i + 1}: ")))

target = int(input("Enter target value: "))

index = binary_search_with_bubble_sort(arr, target)

print("Sorted list:", arr)
if index != -1:
    print("Target found at index:", index)
else:
    print("Target not found (index = -1)")
