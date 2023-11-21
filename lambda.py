# lambda

# def doubled(x):
#     return x*2

# result = doubled(22)
# print(result)


doubled = lambda num : num*2
# result = doubled(22)

# square = lambda num : num*num
# result2 = square(2)
# print(result, result2)

# add = lambda num1, num2 : num1 + num2
# result = add(2, 4)
# print(result)

numbers = [12, 40, 50, 66, 56, 29, 91]
# doubled_numbers = map(doubled, numbers)
doubled_numbers = map(lambda x: x*2, numbers)
squared_numbers = map(lambda x: x*x, numbers)
print(numbers)
print(list(doubled_numbers))
print(list(squared_numbers))

actors = [
    {'Name' : 'Naim', 'Age' : 23}, 
    {'Name' : 'Amit', 'Age' : 32}, 
    {'Name' : 'Shahin', 'Age' : 22}, 
    {'Name' : 'Fahad', 'Age' : 40}, 
    {'Name' : 'Tonmoy', 'Age' : 25}, 
]

juniors = filter(lambda x : x['Age'] < 30, actors)
fivers = filter(lambda x:x['Age'] % 5 == 0, actors)
print(list(juniors))
print(list(fivers))
