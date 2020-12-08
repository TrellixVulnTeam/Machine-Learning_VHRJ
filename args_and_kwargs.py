def super_func(*args, **kwargs): #the stars allos to accepts any number of arguments when printing
    total = 0
    print(kwargs)
    for items in kwargs.values():
        total +=items
    return sum(args) + total
print(super_func(1,2,3,4,5, num1 = 5, num2 = 10))

#*args allows us to grab the postional arguments 1,2,4,5
#kwargs any number of arguments, get a dictionary

#Rules: def (params, *args, default parameter, **kwargs
    #print(params, .....)