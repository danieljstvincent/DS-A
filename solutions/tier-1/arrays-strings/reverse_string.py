def reverse_string(s):

    rev_string = ""
    for i in s:
        rev_string = i + rev_string
    return rev_string


print(reverse_string("alsdkfj"))