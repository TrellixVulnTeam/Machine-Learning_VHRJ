untest = {'a':1,'b':2}
print(untest['b']) #the value that is stored in b, grab it.

dictionaire = {
    'a': [1,2,3],
    'b': 'hello',
    'x': True

}

print(dictionaire)

my_list = [{
    'a': [1,2,3],
    'b': 'hello',
    'x': True
    },
    {
    'a': [4,5,6],
    'b': 'hello',
    'x': True
}
]
print(my_list[0]['a'][2]) #in the first item of the array, grab the 3rd item in a
print(dictionaire['a'][1])

#Dictionbary keys
user_arne = {
    'basket' : [1,2,3],
    'greet' : 'hello'
}
#print(user_arne['age']) # when unknown values, can I get the age?y/n
#use the method of get so the program does not erro
print(user_arne.get('age', 99)) #if does not exist, use 99 as default value


user2 = dict(name='JohnJohn')
print(user2)