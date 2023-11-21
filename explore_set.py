# list --> []
# tuple --> ()
# set --> {}
# set: collection of unique items also mutable. no duplicate
numbers = [10,20,30,405,60,50,201,10,20,30]
print(f'This is a List: {numbers}')
set_making = set(numbers)
print(f'This is a set: {set_making}')
set_making.add(100)
print(set_making)
set_making.remove(201)
print(set_making)
for set_item in set_making:
    print(set_item)

if 0 in set_making:
    print('0 is Exist')
elif 10 in set_making:
    print('You Boom')

A = {1, 2, 3}
B = {1, 3, 5, 7}
print(A&B) #A intersection B
print(A|B) #A union B

#some methods of set
# https://docs.python.org/3.10/library/stdtypes.html#set-types-set-frozenset