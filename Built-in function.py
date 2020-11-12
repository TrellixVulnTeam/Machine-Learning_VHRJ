print(len('hellloooooo')) 

greet = 'helloo'
print(greet) 

print(greet[0:len(greet)])

quote = 'to be or not to be' 
#using the built-in functon to caputalize
print(quote.upper())

print(quote.capitalize())

#lower case
print(quote.lower())

#find 
print(quote.find('be'))

#replace
print(quote.replace('be', 'me'))

print(quote) #the original quote will display since strings are immutable.

quote2 = quote.replace('be', 'me')
print(quote2)