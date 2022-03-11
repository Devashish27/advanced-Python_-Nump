'''

Iterable    :      
Iteration   :
Iterator    :

'''


def gen(n):
    for i in range(n):
        yield i


# for i in range(10000):
# print(gen(10000))

ob1 = gen(100)
# print(next(ob1))
# print(next(ob1))
    # print(i)

# for i in gen(100):
#     print(i)

num = "Tyron"
iter1 = iter(num)

print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))

# for i in num:
#     print(i)
