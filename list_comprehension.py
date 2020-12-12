my_list = [char for char in 'Hello']
print(my_list)

my_list2 = [num for num in range(0,100)]
print(my_list2)

#If i want to multiply each num by 2
my_list3 = [num * 2 for num in range(0,100)]
print(my_list3)

my_list4 = [num ** 2 for num in range(0,100) if num % 2 == 0]
print(my_list4) # if we only want to keep even num.



simple_dict = {
    'a' : 1,
    'b' : 2
}
my_dict = {num:num * 2 for num in [1,2,3]}
print(my_dict)