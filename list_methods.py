basket = [1,2,3,4,5]
print(len(basket ))

#adding
basket.append(100) #append the basket
new_basket = basket
print(new_basket) 

#inserting
basket.insert(4, 100) #add a 100 at the index of 4
new_basket = basket
print(new_basket)

#extending
basket.extend([100, 102]) # extending or adding 2 more items to the list    
new_basket = basket
print(new_basket)


