total = 0 # it represents the global total

def count(total):
    #global total - Instead of using global if file is larger,pass total in count
    total += 1
    return total
print(count(count(count(total))))