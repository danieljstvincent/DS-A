def pair_sum(numbers, target_sum):
    previous_numbers = {}

    for index, num in enumerate(numbers):
        complement = target_sum - num

        if complement in previous_numbers:
            return (index, previous_numbers[complement])

        previous_numbers[num] = index

print(pair_sum([3, 2, 5, 4, 1], 8))  # -> (0, 2)
