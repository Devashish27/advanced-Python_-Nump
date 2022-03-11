'''



'''

users = ['Harshal', 'Preveen', 'Rahul', 'Karim', 'Lalith']
computer = ['Rasberri-pi', 'android', 'Iphone', 'Windows', 'Normal xp']

# for i in range(0, len(users)):
#     print("computer used by ", users[i], " ia ", computer[i])

for i in range(0, len(users)):
    # template = "Computer Used By {} is {}".format(users[i], computer[i])
    # template = "Computer Used By {} is {}"
    template = "Computer Used By {1} is {0}"  # This will turn reverse
    print(template.format(users[i], computer[i]))

