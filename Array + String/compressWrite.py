# compressWrite a function, compress, that takes in a string as an argument. The function should return a compressed version of the string where consecutive occurrences of the same characters are compressed into the number of occurrences followed by the character. Single character occurrences should not be changed.



# test_00
print(compress('ccaaatsss')) # -> '2c3at3s'
# test_01
compress('ssssbbz') # -> '4s2bz'
# test_02
compress('ppoppppp') # -> '2po5p'
# test_03
compress('nnneeeeeeeeeeeezz') # -> '3n12e2z'