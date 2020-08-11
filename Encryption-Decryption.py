print("==========Welcome to the Encryptor-Decryptor==========")

print('''
1. Encryption 1
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

        if x.isdigit():
            e_password = e_password + chr(ord(x) - 14)

        position += 1

    print('Encryption:', e_password)
