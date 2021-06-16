#Task1
#created a list
A = [1, 2, 5]
print(A)
#Added an item
A.append(6)
print(A)
#deleted a item
del A[:1]
print(A)
#max & min number of list stored in variables
b = max(A)
c = min(A)
print(b)
print(c)
#Task2
#created a tuple
t = (7, 'u', 9, 'k')
print(t)
#revesed that tuple
print('After reversing the tuple:', t[::-1])
#Task3
#converted tuple into list
print('Type of t is:',type(t))
l=list(t)
print('Type of l is:',type(l))
print(l)
