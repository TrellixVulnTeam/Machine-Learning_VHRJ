#check if driver is old, ID holder.

is_old = False
is_licensed = True

if is_old:
    print('You are old enough to drive!')
elif is_licensed:
    print('You are old enough to drive!')
else:
    print('You cant drive!')
print('Check again!')
 

 #Simpler way
if is_old and is_licensed:
    print('You are old enough to drive') #Both condition should be true
else:
    print('Check again!')