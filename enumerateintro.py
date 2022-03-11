a = ['CodeWithTyron', 'Max-Series', 'Anime', 'Star-movies', 'HBO', 'Remedy-Now']
# i = 0
# for item in a:
#     i = i + 1
#     if i % 2 == 0:
#         print(item)

for i, item in enumerate(a):
    if (i+1) % 2 == 0:
        print(i, item)
