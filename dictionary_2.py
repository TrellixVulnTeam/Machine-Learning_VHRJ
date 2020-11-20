user = {
    'basket' : [1,2,3],
    'greet' : 'hello',
    'age' : 20
}
print('size' in user.keys()) #basket, gree and age are keys. values are hello, 20...
print('hello' in user.values()) 
print(user.items())

print(user.pop('age')) #remove value

print(user.update({'age' : 60}))
print(user) #display without the popped value.