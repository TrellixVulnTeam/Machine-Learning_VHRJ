amazon_cart = [
    'notebokks',
    'sunglasses',
    'toys',
    'grapes'
]

#replace notebooks by laptops
amazon_cart[0] = 'laptop'
new_cart = amazon_cart[:] #amazon cart will stay the same at display, new cart will have gum on 
#firt index due to the colon
new_cart[0] = 'gum'
print(new_cart)
print(amazon_cart) 

#lists are mutable unlike strings.

