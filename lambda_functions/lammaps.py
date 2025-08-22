#square each number in a list using maps
nums = list(range(1,21))
print(nums)
sqr_nums =list(map(lambda x: x**2, nums))
print(sqr_nums)

#testing each number in a list
nums = list(range(1,11))
print(nums)
even = list(map(lambda x: x%2 ==0, nums))
print(even)


#Modifying a list of tuples
teams =  [('Kenya', 23), ('Germany', 20), ('Uganda', 35), ('Italy', 19), \
   ('Argetina',17),('France', 12),('England',33)]
print(teams)

new = list(map(lambda team: (team[0], team[1]+1), teams))
print(new)
