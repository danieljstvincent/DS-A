#uncompress and Write a function, uncompress, that takes in a string as an argument. The input string will be formatted into multiple groups according to the following pattern:
# When we find a char in string we print that char the number amount of times.
# Determine if it is a number.Determine
# Contactain the number if there is more the one
# Print that many charaters
#
def uncompress(s):
    uncompressed_string = ''
    result = []
    # numbers = [1,2,3,4,5,6,7,8,9]
    i = 0
    j = 0

    while i < len(s):
        if s[j].isdigit():
            j += 1
        else:
            num = int(s[i:j])
            result.append(s[j] * num)
            j += 1
            i = j

    return ''.join(result)


#
# for example, '2c' or '3a'.
# The function should return an uncompressed version of the string where each 'char' of a group is repeated 'number' times consecutively. You may assume that the input string is well-formed according to the previously mentioned pattern.
# test_00
print(uncompress("2c3a1t")) # -> 'ccaaat'
# test_01
print(uncompress("4s2b")) # -> 'ssssbb'
# test_02
print(uncompress("2p1o5p")) # -> 'ppoppppp'
# test_03
print(uncompress("3n12e2z")) # -> 'nnneeeeeeeeeeeezz'
# test_04
print(uncompress("127y")) # -> 'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'