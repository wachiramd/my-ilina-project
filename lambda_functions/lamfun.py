print("input number to be squared")
result = int(input())
squared = lambda x: x**2 #here you can use any variable you want.
outpt = squared(result)
print(outpt) 
print(squared(result)) #directly prints the output of a function

print("input the numbers to be added together")
m = int(input())
n = int(input())
add = lambda m, n: m+n

print(add(m,n))

print("input the numbers to be multiplied together")
a = int(input())
print("the second number")
b = int(input())
print("input the third number")
c = int(input())
multiply = lambda j,k,l : j*k*l
print(multiply(a,b,c))

#using default values
print("input the value you want squared")
t = int(input())
s = int(input())
power = lambda t, s: t**s
print(power(t))
