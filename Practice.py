def highest_even(li):
    even_numbers = []  # create empty list for even numbers
    for item in li:
        if item % 2 == 0:
            even_numbers.append(item)
    return max(even_numbers) #return from the loop, hence indentation.


print(highest_even([10,2,3,4,8,11])) #no need to ask for user input