my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}
 
 #print elements that are not the same
print(my_set.difference(your_set)) 
print(my_set)

 #gets rid of 5
print(my_set.discard(5))
print(my_set)

 #similar 
print(my_set.intersection(your_set))

 #do they have anything in common?
print(my_set.isdisjoint(your_set))
#is my set inside of your set?
print(my_set.issubset(your_set))
#is my set a superset of your_set?
print(my_set.issuperset(your_set))
