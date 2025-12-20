def quick_sort(arr):
    if len(arr) <= 1:                    # Base case: Array with 0 or 1 element is already sorted
        return arr
    pivot = arr[-1]                      # Choose the last element as the pivot
    smaller = [x for x in arr[:-1] if x <= pivot]  # Elements <= pivot
    larger = [x for x in arr[:-1] if x > pivot]    # Elements > pivot
    return quick_sort(smaller) + [pivot] + quick_sort(larger)  # Combine sorted halves
