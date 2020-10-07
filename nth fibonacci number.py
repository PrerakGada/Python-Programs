number=int(input("Ehich fibonacci number do you want to find?::"))
a=-1
b=1
for i in range(1,number+1):
    c=a+b
    #print(c," ",end="")
    a=b
    b=c
    if i==number:
        print(i,"th fibonacci number is:",c)
