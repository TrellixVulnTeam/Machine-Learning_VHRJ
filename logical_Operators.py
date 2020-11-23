is_magician = True
is_expert = True

#mangician and expert
if is_magician and is_expert:
    print('You are a master magician')
# mangician but not expert
elif is_magician or is_expert:
    print('At least, you are getting there!')

else:
    print('You need magic!')