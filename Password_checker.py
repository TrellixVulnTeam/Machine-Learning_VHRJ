#ask for the user name
# input for password
#print hidden user name, password and the lengths.

user_name = input('What is your user name? ')
password = input('What is the password? ')

# in order to hide the password:
password_length = len(password)
hidden_password = '*' * password_length

print(f'{user_name}, your password, {hidden_password}, is {(password_length)} letters long')
