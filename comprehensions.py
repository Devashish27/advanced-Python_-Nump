'''

List Comprehensions
Dictionary Comprehensions
Set Comprehensions
Generator Comprehensions

'''

list_1 = [3, 5, 754, 3, 75, 5, 97, 44, 85, 3, 7, 74, 5, 53, 45, 6, 7, 7, 7, 6, 5, 43, 5]

divide_by_3 = []

for item in list_1:
    if item % 3 == 0:
        divide_by_3.append(item)

print('Without Using List Comprehensions', divide_by_3)
print("Using List Comprehensions", [item for item in list_1 if item % 3 == 0])

# Dict_comp
dict1 = {'a': 53, 'b': 56, 'A': 8}
print({k.lower(): dict1.get(k.lower(), 0) + dict1.get(k.upper(), 0) for k in dict1.keys()})

squared = {x ** 2 for x in [1, 2, 3, 4, 5, 7, 87, 2, 3]}
print(squared)

gen = (i for i in range(35) if i % 3 == 0)
# print(gen)
for item in gen:
    print(item)
