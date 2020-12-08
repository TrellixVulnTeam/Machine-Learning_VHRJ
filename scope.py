# Scope -  what variables do I have access to?

if True:
    x = 10 # 10 is part of the world of 100

def some_func():
    total = 100
print(x)


#SCOPE RULES:

a = 1

def confusion():
    a = 5
    return a

print(a)
print(confusion())

print(confusion())
print(a)
