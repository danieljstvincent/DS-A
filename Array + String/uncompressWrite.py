#uncompress and Write a function, uncompress, that takes in a string as an argument. The input string will be formatted into multiple groups according to the following pattern:
# When we find a char in string we print that char the number amount of times of the previous charter
# Determine if it is a number.Determine
# Contactain the number if there is more the one
# Print that many charaters
#
def uncompress(s):
    new_char = ''
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for i in s:
        if i == numbers
            new_char = i(s[-1])

    pass  # todo
#
# for example, '2c' or '3a'.
# The function should return an uncompressed version of the string where each 'char' of a group is repeated 'number' times consecutively. You may assume that the input string is well-formed according to the previously mentioned pattern.
# test_00
# uncompress("2c3a1t") # -> 'ccaaat'
# test_01
# uncompress("4s2b") # -> 'ssssbb'
# test_02
# uncompress("2p1o5p") # -> 'ppoppppp'
# test_03
# uncompress("3n12e2z") # -> 'nnneeeeeeeeeeeezz'
# test_04
# uncompress("127y") # -> 'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'