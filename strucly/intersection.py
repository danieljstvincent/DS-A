# Create a new new_list

#Method 1
# Create a nested for loop and compare if that compare the int in each list and if a int is is the second list add it to the new list

#Method 2
# I know that a set does not allow duplicates, we what to find the duplicates and add them to the new list. So if a number is part of a set we will add it to the new list.


def intersection(a, b):
    new_list = []
    for i in a:
        if i in b and i not in new_list:
            new_list.append(i)
    return new_list

print(intersection([4,2,1,6], [3,6,9,2,10]))  # Output: [2, 6]


# Create a new new_list

# Method 1
# Create a nested for loop and compare if that compare the int in each list and if a int is is the second list add it to the new list

# Method 2
# I know that a set does not allow duplicates, we what to find the duplicates and add them to the new list. So if a number is part of a set we will add it to the new list.


def intersection(a, b):
    result = []
    item_set = set()

    for item in a:
        items_set.add(items)

    for ele in b:
        if ele in items_set:
            result.append(ele)

    return result
