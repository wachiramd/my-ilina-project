#using reduce to sum a list of numbers
from functools import reduce

nums = list(range(1,21))
total = reduce(lambda x,y: x+y, nums)
print(total)
print(sum(nums)) #same as the reduce function above

#Multiplicaiton using reduce

numbers = list(range(1,21))
total_m = reduce(lambda x, y: x*y, nums)
print(total_m)

num2 = [1,2,3]
print(reduce(lambda x,y:x+y,num2))
