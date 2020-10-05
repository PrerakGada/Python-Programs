


from functools import reduce


nums = [5,3,9,2,7,3,1,8,6,3,1,4,7,8,4,2,6,2,1,6]

even = list(filter(lambda n : n%2==0, nums))

double = list(map(lambda d : d*2, even))

sum = reduce(lambda a,b : a+b,double)

print(even)
print(double)
print(sum)





 
