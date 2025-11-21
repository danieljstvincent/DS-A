arr = [2, -7, -2, -2, 0]

def absSort(arr):
    n = len(arr)
    for i in range(n):           # O(n) iterations
        min_index = i
        for j in range(i + 1, n): # O(n-i) iterations
            # Comparisons happen here
            if abs(arr[j]) < abs(arr[min_index]):
                min_index = j
            elif abs(arr[j]) == abs(arr[min_index]):
                if arr[j] < arr[min_index]:
                    min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]  # O(1) swap
    return arr

print(absSort(arr))