# task1: creat 2 dict & add them
grp = {"97": "urvi", "98": "sobhit", "99": "jay"}
grp1 = {'100': 'Parikshit', '101': 'Heena', '102': 'Shivam'}
dict = {**grp, **grp1}
print(dict)
# task2: remove 1 key from dict
del dict["98"]
print(dict)
# task3: Map two list into a dict
En_no = ['100', '101', '102']
Name = ['Parikshit', 'Heena', 'Shivam']
dict1 = {En_no[0]: Name[0], En_no[1]: Name[1], En_no[2]: Name[2]}
print(dict1)
# task4: find length of a set
set = {"nida", "dharam", "dhara"}
print(len(set))
# task5: remove intersection of set1 from set
set1 = {"nida", "urvi", "heena"}
new_set = set - set1
print(new_set)
