def func(a,b):
    return a+b
a=["Hello","Hi","Good"]
b=["World","Everyone","Morning"]
c=zip(a,b)
print(tuple(c))

#
lst1=["Good", "Bad", "Happy", "Sad", "High", "Low", "Medium"]


#Type your answer here.

rng1=list(range(1,8))

lst =zip(lst1,rng1)

print(lst)


#
a=[20,5,16,90,55,4]
c=sorted(a)
print(c)


#
num=[16,90,55,4,15]
print("Original List Of a : ",num)
print("Even Numbers from the Given List :")
even_num=list(filter(lambda x:x%2==0,num))
print(even_num)
print("Odd Numbers from the Given List :")
odd_num=list(filter(lambda x:x%2!=0,num))
print(odd_num)