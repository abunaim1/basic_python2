# key value pair
# dictionary
# object
# hash table
# overlap with set
# {key:value, key:value, key:value}

person1 = {'Name':'Abu Naim', 'Age': 23, 'Profession': 'Baker' }
print(person1)
print(person1['Name'])
print(person1.keys())
print(person1.values())

person1['Language'] = 'Hibru'
person1['Name'] = 'Sada Pakhi'
print(person1)
del person1['Age']
print(person1)

# special dictionary looping
for key,value in person1.items():
    print(key,':', value)

# more about dictionnary methods
# https://docs.python.org/3/tutorial/datastructures.html#dictionaries