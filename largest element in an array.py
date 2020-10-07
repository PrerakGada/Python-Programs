from array import *

arr=array("i",[])
number=int(input("How many number do you want to entered in array?::"))
print("Enter",number,"numbers:")

for i in range(number):
    x=int(input())
    arr.append(x)
    
max=arr[0]
min=arr[0]
sum=0

for e in arr:
    if e>max:
        max=e
    if e<min:
        min=e

for e in arr:
    sum+=e

print("maximum number is:{0}".format(max))
print("minimum number is:{0}".format(min))
print("Sum of array is:{0}".format(sum))
