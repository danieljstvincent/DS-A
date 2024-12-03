def length_of_longest_substring(s: str) -> int:
    # Initialize a dictionary to store the last seen index of each character
    char_index_map = {}
    
    # Variables to track the start of the current window and the maximum length
    start = 0
    max_length = 0
    
    # Iterate over the string with the index and character
    for end, char in enumerate(s):
        # If the character is already in the dictionary and its index is within the current window
        if char in char_index_map and char_index_map[char] >= start:
            # Move the start of the window right after the last occurrence of the repeating character
            start = char_index_map[char] + 1
        
        # Update the last seen index of the current character
        char_index_map[char] = end
        
        # Calculate the length of the current window and update the maximum length if needed
        max_length = max(max_length, end - start + 1)
    
    return max_length

# Example calls
result1 = length_of_longest_substring("pwwkew")
result2 = length_of_longest_substring("abcabcbb")
result3 = length_of_longest_substring("bbbbb")
result4 = length_of_longest_substring("")

# Print results
print(result1)  # Output: 3 (substring: "wke")
print(result2)  # Output: 3 (substring: "abc")
print(result3)  # Output: 1 (substring: "b")
print(result4)  # Output: 0 (substring: "")
