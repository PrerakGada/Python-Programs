list=[]
number=int(input("How many number do you want to enter:"))
for i in range(1,number+1):
    x=int(input("Enter {} element:".format(i)))
    list.append(x)
print("Your list is:",list)
max=list[0]
s_max=list[0]
min=list[0]
for e in list:
    if e>max:
        max=e
    else:
        s_max=max
    if e<min:
        min=e
        
"""
for i in range(max-1,0,-1):
    for e in list:
        if e<max and e>i:
            s_max = e;
            break
"""
print("Second max:",s_max)


print("Maximum element is:",max)
print("Minimum element is:",min)
