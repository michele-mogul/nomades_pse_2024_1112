import my_array
import random

# print(my_array.sum([1, 2, 3, 4, 5]))


l = [5, 5, 5, 4, 4, 3, 3, 2, 1]
random.shuffle(l)
l2 = l

l2.append(38)
print(sorted(l), l, sep="\n")

print(my_array.sort_descending(l))