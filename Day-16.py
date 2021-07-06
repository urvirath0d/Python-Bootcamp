#
# Finding Value of lambda a
x=lambda a:a+50
print(x(5))


#
# Addition of two numbers using lambda
x=lambda a,b:a+b
print(x(10,5))


#
#subtraction of two numbers using lambda
x=lambda a,b,c:a-b-c
print(x(10,2,4))


#
# Multiplying the lambda arguments using def function
def fun1(n):
    return lambda a:a*n
mydoubler = fun1(5)
print(mydoubler(10))


#
# Filter in lambda
lst=[10,20,30,36]
tuple(filter(lambda x:(x%3 == 0),lst))


#
# Map in Lambda
lst=[10,20,30,36]
list(map(lambda x:(x**2),lst))


#
# Multiplication of two arguments in lambda function
a=lambda x,y:x*y
print(a(5,6))


#
from functools import reduce
fibo = lambda n:reduce(lambda x, _:x+[x[-1]+x[-2]],range(n-2),[4,1])
print("Fibonacci Series upto 5:")
print(fibo(10))


#
# Multiplying each number in list with a given number
lst=[12,15,27,34,55]
n=2
print("Original list :",lst)
print("Given Number :",n)
filtered_numbers=list(map(lambda number:number*n,lst))
print("Result:")
print("Result :")
print(' '.join(map(str,filtered_numbers)))



#
lst=[33,45,63,88,99,114]
print("The Number  Which are Divisible by 9 in list :")
list(filter(lambda x:(x%9==0),lst))



#
lst=[1,4,9,14,20]
count_even=0
for x in lst:
    if x%2 ==0:
        count_even+=1
print("No.of Even Numbers :",count_even)