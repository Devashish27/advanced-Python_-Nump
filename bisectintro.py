import bisect

number = 5

a = [1, 2, 6, 76, 3 ,8, 3 ,9,46]  # If the list is not sorted then bisect module will become wrong...!

print(bisect.bisect(a, number))

bisect.insort(a, number)
print(a)

# print(a)
