def multiple():
    return 3,4
print(multiple())
things = 'walet', 'smoke', 'headphone', 'ash tra', 'water bottle', 'cigrrates'
# print(type(things))
# print(things)
# print(things[::-1])
# print(things[-3::-1])
# print(things[0:4])
# for item in things:
#     print(item)
# if 'walet' in things:
#     print('Exist')

# things[0] = 'pen' # this is also gives error beacuse tuple is also immutable
# print(things)

# print(len(things))
mega = ([1,3,4,7], [9,8,7,7])
# print(mega)
# print(type(mega))

# tuple is immutable but if a [list] staying inside a tuple this [list] could be mutable/changable for example,
mega[0][1] = 666 #mega er zero index e je ache tar 1 number index e 666 boshai dilam
print(mega) 

# some methods of tuple:
# https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences