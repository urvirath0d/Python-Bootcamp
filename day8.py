# task1
# Write a program script to merge two python dictionaries
dict1 = {"97": "urvi", "99": "vishvash"}
dict2 = {"95": "parikshit", "96": "jay"}
print(dict1, "\n", dict2)
dict3 = {**dict1, **dict2}
print("After merging two dictionaries:", dict3)
# task2
# Write a program to sort the value from descending to ascending in list and convert it in to a set.
list1 = [1, 7, 0]
print("Original List:", list1)
list2 = sorted(list1, reverse=False)
print("After sorting the value Of list from descending to ascending:", list2)
# Converting List into set
s = set(list2)
print("Converting List into set:", (s, type(s)))
# tak3
# Write a Python program to list number of items in a dictionary key and
# sort the list with the help of a function & without the function.
print("The original dictionary is : ", dict3)
print("List Of All the keys of dictionary is:", dict3.keys(), "\nThe sorted dictionary key list is:",
      sorted(dict3.keys(), reverse=True))
print("The sorted dictionary is:", dict(sorted(dict3.items(), reverse=True)))
# task4
# Write a Python program to get a string from a given string (user input) and
# change the first occurrence of the word to a user specified input.
str1 = input("Enter Your Name:")
print(str1)
str2 = input("Enter a string You want to change")
print("Modified string :", str1.replace(str1[0], str2[0:]))
# task5
# Write a Python program to get a string from a given string where all occurrences of
# its first char have been changed to capital letter.
str3 = str1.capitalize()
print("first char has been changed to capital letter:", str3)
# task6
# Write a Python program to find the repeated items of a list
list3 = [1, 3, 5, 3, 6, 5, 10, 10, 12, 14, 14]
list4 = []
list5 = []
j = None
print(list3)
for i in list3:
    if i not in list4:
        list4.append(i)
    else:
        j = i
        list5.append(j)
print(list5)
# task7
# Write a Python program to check the sum of three elements and
# divided by a value which is given as an input by the user
a = int(input("enter 1 no"))
b = int(input("enter 2 no"))
c = int(input("enter 3 no"))
print("sum of three elements :", (a + b + c))
print("divided by a value :", (a + b + c) / a)
# task8
# Write a Python program to find the Mean,median,mode among three given numbers
l1 = [1, 4, 6, 9, 3, 1, 5]
x = len(l1)
l2 = sorted(l1, reverse=False)
print("Mean Of Given numbers is:", sum(l1[0:]) / x)
# for finding median
if x % 2 != 0:
    ans = int(x / 2)
    print("median Of Given numbers is:", l2[ans])
else:
    ans1 = int((x - 2) / 2)
    ans2 = int(x / 2)
    answer = float((l2[ans1] + l2[ans2]) / 2)
    print("Median Of Given numbers is:", answer)


# for finding mod
def mode1(numbers):
    mode = max(numbers, key=numbers.count)
    return mode


print("mod Of Given numbers is:",mode1(l1))
# task 9
# Write a Python program to swap cases of a given string
str1 = input("Enter your name:")
print("After Swapping your name:", str1.swapcase())
# task 10
# Write a program to convert an integer to binary & octa decimal
a = int(input("Enter a integer"))
bi = bin(a)
oc = oct(a)
print("integer into binary is:", bi, "\ninteger into octa decimal is :", oc)
