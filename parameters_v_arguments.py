# parameters are name and emoji
def say_hello(name = 'Papa', emoji = ';)'):
    print(f'Helloooo {name}, {emoji}')

#arguments are Arne and :)
say_hello('Arne', ':)')
say_hello('Danna', ':)')
say_hello('Mafille', ':)')
say_hello('Ryan', ':)')

#Hey words arguments
say_hello(name ='Ken', emoji = '))')

#default parameters go into the defined function
say_hello(name ='Ken', emoji = '))') #Will not print
say_hello() #will print default since brckts empty.