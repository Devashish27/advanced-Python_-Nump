'''

Syntax:
lambda Argument: Manipulate(Argument)

'''


# def add(a, b):
#     s = a + b
#     return s

# Using Lambda.!
# add = lambda x, y: x + y
# add = lambda x, y: x > y
#
#
# print(add(2, 7))


# Example:
# a = [(1, 2), (4, 5), (555, 57)]
# a.sort(key=lambda x: x[1])
#
# print(a)


# Other type..!
def x(val):
    return val[1]


a = [(1, 2), (4, 5), (555, 57)]
a.sort(key=x)

print(a)
