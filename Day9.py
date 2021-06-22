# Task-1
# Write a program to loop through a list of numbers and
# add +2 to every value to elements in list
list1 = [1, 5, 9, 10, 3]
list2 = []
for i in list1:
    i = i + 1
    list2.append(i)
print(list2)
# Task-2
# Write a program to get the below pattern
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end="")
    print()
# Task-3
# Python Program to Print the Fibonacci sequence
n = int(input("How many terms you want? :"))
# first two terms
n1 = 0
n2 = 1
count = 0
# check if the number of terms is valid
if n <= 0:
    print("Plese enter a positive integer")
elif n == 1:
    print("Fibonacci sequence:")
    print(n1)
else:
    print("Fibonacci sequence:")
    print(n1, ",", n2, end=' , ')
    while count < n:
        nth = n1 + n2
        print(nth, end=' , ')
        n1 = n2
        n2 = nth
        count += 1
# Task-4
# Explain Armstrong number and write a code with a function
num=int(input("Enter a Number :"))
sum=0
temp=num
while temp>0 :
    digit=temp % 10
    print(digit)
    sum=sum+digit**3
    print(sum)
    temp=temp//10
    print(temp)
if num==sum:
    print("It is an Armstrong")
else:
    print("It is not Armstrong")
# Task-5
# Write a program to print the multiplication table of 9
n=9
a= int(input("Enter a number: "))
for i in range(1,a+1):
    print(n,'x',i,'=',i*n)
#Task-6
# Check if a program is negative or positive
n=int(input("Enter a Number :"))
if (n>0) :
    print("It is a Positive Number")
elif (n<0):
    print("It is a Negative Number")
else:
    print("It is a zero")
# Task-7
# Write a program to convert the number of days to ages
d= int(input("Enter the days:"))
# Conversion of days in to years, weeks and days
y = int(d / 365)
w = int((d % 365) / 7)
t = int(d-(y*365+w*7))
print("Age :",y, " Year, ", w, " Weeks, and ", t, " Days\n")
#Task-8
# Solve Trigonometry problem using math function write a program to solve using math function
import math
a=int(input("Enter a Value :"))
print("The value of the sine is :",math.sin(a))
print("The value of the cosine is :",math.cos(a))
print("The value of the tan is :",math.tan(a))
#Task-9
# Create a calculator only on a code level by using if condition (Basic arithmetic calculation)
num1=float(input("Enter First Number :"))
num2=float(input("Enter second Number :"))
print("Select the operator :")
print("1.Addition \n 2.Subtraction \n 3.Multiplication \n 4.Division")

n=int(input("Select Your Choice (1/2/3/4) :"))
one=1
two=2
three=3
four=4
if n==one:
    print("Addition of Two Number is :",num1,"+",num2,"=",(num1+num2))
elif n==two:
    print("Subtraction of Two Numbers is :",num1,"-",num2,"=",(num1-num2))
elif n==three:
    print("Multiplication of Two Numbers is :",num1,"*",num2,"=",(num1*num2))
elif n==four:
    print("Division of Two Numbers is :",num1,"/",num2,"=",(num1/num2))
else:
    print("invalid choice")


