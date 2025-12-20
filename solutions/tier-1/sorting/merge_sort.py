def merge_sort(arr):
    if len(arr) > 1:                     # Base case: If array length <= 1, it's already sorted
        mid = len(arr) // 2              # Find the midpoint
        left_half = arr[:mid]            # Divide the array into left half
        right_half = arr[mid:]           # Divide the array into right half

        merge_sort(left_half)            # Recursively sort the left half
        merge_sort(right_half)           # Recursively sort the right half

        i = j = k = 0                    # Pointers for left_half, right_half, and main array
        while i < len(left_half) and j < len(right_half):  # Compare elements in left and right halves
            if left_half[i] < right_half[j]:               # Pick the smaller element
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):        # If elements are left in the left_half, add them
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):       # If elements are left in the right_half, add them
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr                           # Return the sorted array
