#for i,char in enumerate('Helloooooo'):
 #   print(i, char) #index of each item 

for i, char in enumerate(list(range(100))):
    if char == 50:
        print(f'The index of 50 is: {i}')