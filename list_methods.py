basket = [1,2,3,4,5]
print(len(basket))

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


#removing an item, I can pop(0)
basket.pop ()
new_basket = basket.extend([100])
print(basket)

#I can use .remove
basket1 = [2,4,6,8,10]
print(len(basket1))
new_basket1 = basket1.remove(6)
print(basket1)

