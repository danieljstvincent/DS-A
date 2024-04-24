def five_sort(nums):
    five_at_the_end = []

    # Iterate through each item in the list
    for item in nums:
        if item != 5:
            # If the item is not 5, append it to the result list
            five_at_the_end.append(item)

    # Append all occurrences of 5 to the end of the result list
    five_count = nums.count(5)
    five_at_the_end.extend([5] * five_count)

    return five_at_the_end

print(five_sort([12, 5, 1, 5, 12, 7]))