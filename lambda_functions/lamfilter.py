#filtering a lisy of numbers
nums = list(range(1,21))
print(nums)
evens=list(filter(lambda x:x%2==0, nums))
odds = list(filter(lambda x:x%2 !=0, nums))
print(evens)
print(odds)

numbers = [1,2,3]
print(list(filter(lambda x: x>1, numbers)))

from statistics import mean
data = list(range(1,51))
avg = mean(data)
above_avg = list(filter(lambda x: x>avg, data))
below_avg = list(filter(lambda x: x<avg, data))
print(data)
print(avg)
print(above_avg)
print(below_avg)
