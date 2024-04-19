# dic key is the letter and the value is the count. We could store the largest count


def most_frequent_char(s):
    count = {}
    for char in s:
        if char not in count:
            count[char] = 0
        count[char] += 1
    return count

print(most_frequent_char('bookeeper')) # -> 'e'
print(most_frequent_char('david')) # -> 'd'
print(most_frequent_char('abby') )# -> 'b'
