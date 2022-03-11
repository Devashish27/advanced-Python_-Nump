# * args and ** kwargs Tutorial...!!
# * vars and ** kvars tutorial..!!

def function_1(*argsjoke):  # We Can Take as *args for name, age, rollno

    # print(type(args))

    if len(argsjoke) == 3:
        print("The Name Of The Student is ", argsjoke[0], "and age is ", argsjoke[1], "and rollno is ", argsjoke[2])
    else:
        print("The Name Of The Student is ", argsjoke[0], "and age is ", argsjoke[1])


def printmarks(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(key, value)


def master(normal, *args, **kwargs):
    print(normal)
    for i in args:
        print(i)
    for key, value in kwargs.items():
        print(key, value)


lis = ["Tyron", 24, 4987453]
# function_1(*lis)
# function_1("Tyron", 24)

marklist = {"Tyron": 100, "Dev": 100, "Sharuk": 89, "Vikranth": 98, "Vikram" : 82, "Harish": 82, "Srinivas": 78}

# printmarks(**marklist)
print(master("normal arg", *lis, **marklist))