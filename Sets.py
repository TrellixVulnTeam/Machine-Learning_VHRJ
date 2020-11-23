my_set = {1,2,3,4,5,5}
my_set.add(100)
my_set.add(2) #wont be added since it is in the set in one location in the memory.
print(my_set)


#convert into a set from a list
my_array = [1,2,3,4,5,5]
print(set(my_array))

#grab by the actual item in the set
my_set1 = {1,2,3,4,5,5}
print(3 in my_set1)
