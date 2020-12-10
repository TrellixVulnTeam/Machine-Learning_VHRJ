#ef multiply_by2(li):
    #new_list = []
    #for item in li:
     
    #   new_list.append(item*2)
    #return new_list

#print(list(map(multiply_by2, [1,2,3,])))


#cleaner. comment all the top.
#def multiply_by2(item):
#    return item*2
#print(list(map(multiply_by2, [1,2,3])))


# FILTER 

#my_list = [1,2,3]
#def multiply_by2(item):
 #   return item * 2

#def only_odd(item):
 #   return item % 2 != 0

#print(list(filter(only_odd, my_list)))
#print(my_list)


#ZIP

my_list = [1,2,3]
your_list = [10,20,30]
their_list = (4,4,5)
def multiply_by2(item):
    return item * 2

def only_odd(item):
    return item % 2 != 0

print(list(zip(my_list, your_list, their_list)))
print(my_list)