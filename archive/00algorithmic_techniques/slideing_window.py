def sortedSquares(nums):
    square_numbers = []
    sq_int = 0

    for num in nums:
        sq_int = num ** 2
        square_numbers.append(sq_int)
        sorted_square = sorted(square_numbers)
    return sorted_square
        
 
# Example usage
if __name__ == "__main__":
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    print(sortedSquares(nums))  # Output: [3, 3, 5, 5, 6, 7]