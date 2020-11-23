my_tuple = (1,2,3,4,5) #immutable
print(5 in my_tuple)
user = {
    (1,2): [1,2,3],
    'greet' : 'hello',
    'age' : 20
}
print(user[(1,2)])


new_tuple = my_tuple[1:4] #index from 1 to 4
print(new_tuple)    


x,y,z, *other = (1,2,3,4,5)
print(x)
print(other)

print(len(my_tuple)
