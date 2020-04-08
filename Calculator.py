print('--------Welcome to CALCULATOR--------')
c='y'
while(c=='y' or c=='Y'):
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Division')
    print('5. Sqaure')
    print('6. Cube')
    choice=input('Enter the number to do the currosponding operation: ')
    choice=int(choice)

    if(choice==1):
        a=input('Enter the 1st Number: ')
        a=int(a)
        b=input('Enter the 2nd Number: ')
        b=int(b)
        ans=a+b
        print('The Sum is ',ans)

    elif(choice==2):
        a=input('Enter the 1st Number: ')
        a=int(a)
        b=input('Enter the 2nd Number: ')
        b=int(b)
        ans=a-b
        print('The Difference is ',ans)

    elif(choice==3):
        a=input('Enter the 1st Number: ')
        a=int(a)
        b=input('Enter the 2nd Number: ')
        b=int(b)
        ans=a*b
        print('The Product is ',ans)

    elif(choice==4):
        a=input('Enter the 1st Number: ')
        a=int(a)
        b=input('Enter the 2nd Number: ')
        b=int(b)
        ans=a/b
        print('The Quotient is ',ans)

    elif(choice==5):
        a=input('Enter the Number: ')
        a=int(a)
        ans=a*a
        print('The Sqaure is ',ans)

    elif(choice==6):
        a=input('Enter The Number: ')
        a=int(a)
        ans=a*a*a
        print('The Cube is ',ans)

    else:
        print('Wrong Choice!!')
    c=input("Enter 'y' to calculate more: ")
