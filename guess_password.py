import random
import time
import sys
digits = ['1','2','3','4','5','6','7','8','9','0']
lower_case = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
upper_case = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
password = input('Enter the password: ')
print('Generating password...')
print('Please wait...')
password_length = len(password)
password_characters = digits + lower_case + upper_case
print(len(password_characters)**password_length)
attampt = 0
start = time.time()
while True:
    attampt += 1
    gussed_password = ''
    for _ in range(password_length):
        gussed_password += random.choice(password_characters)
    sys.stdout.write(f'\rGuessing password: {gussed_password}')
    sys.stdout.flush()
    time.sleep(0.000001)
    attampt += 1
    if password == gussed_password:
        break
end = time.time()
duration = end - start
time.sleep(2)
print('\nPasssword guess sucessfully ')
print(f'Time taken to guess the password: {duration} seconds')
print(f'Total attempts made: {attampt}')
print('<<<        Password Cracked Successfully         >>>')

