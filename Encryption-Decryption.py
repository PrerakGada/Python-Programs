print("==========Welcome to the Encryptor-Decryptor==========")

# Only Alphanumeric characters and @ _ can be used in password

print('''
1. Encryption
2. Decryption
''')

choice = int(input('Enter Your Choice: '))

if choice == 1:
  password = input('Enter Password: ')
  position = 1
  e_password = ''
  for x in password:

    if x.isalpha():
      i = chr(ord(x) + position)
      e_password += i

    elif x.isdigit():
      e_password = e_password + chr(ord(x) - 14)

    else:
      e_password += x

    position += 1

  print('Encryption:', e_password)

elif choice == 2:
  ep = input('Enter the Encrypted password: ')
  position = 1
  pas = ''

  for x in ep:
    if x.isalpha():
      i = chr(ord(x) - position)
      pas += i

    elif x == '_' or x == '@':
      pas += x

    else:
      pas += chr(ord(x) + 14)

    position += 1

  print('Decryption:', pas)

else:
  print('Wrong Choice!')
