i = 0
while i < 50:
    print(i)
    i = i + 1

# 'for' is for simple loop. If you don't know how long it should loop, use while.

while True:
    response = input(' Say something or bye to break: ')
    if (response == 'bye'):
        break