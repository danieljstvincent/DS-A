def insertion_sort(arr):
    for i in range(1, len(arr)):  # Loop through the array starting from the 2nd element
        print(i,"i")
        current = arr[i]             # The "key" is the current element to be inserted
        j = i - 1                # Start comparing with the previous element
        while j >= 0 and  current < arr[j]:  # While not at the beginning and key is smaller
            arr[j + 1] = arr[j]       # Shift the larger element one position to the right
            j -= 1                      # Move the pointer one step back
        arr[j + 1] =  current                # Insert the key in its correct position
    return arr 

print(insertion_sort([50,52,43,39,22,14,9]))
#                      j  i
# 
# #
