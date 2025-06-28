sample_list = [1, 2, 3, "apple", "banana", True, False, 4.5, ["nested", "list"]]
copied_sample_list = sample_list.copy()

#        J
#        |
#2t3o11g2s
#      |
#      I
#output: ttooogggggggggggss
copied_sample_list[4] = "banhana"
print(sample_list)
print(copied_sample_list)

count_sample_list = sample_list.count(9)
print(count_sample_list)