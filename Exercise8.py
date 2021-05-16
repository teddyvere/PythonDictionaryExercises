'''
8. Write a Python script to merge two Python dictionaries.
'''

dict1 = {1:2,3:5,5:7,7:9}
dict2 = {2:4,4:6,6:8,8:10}

dict3 = {}

for item in (dict1,dict2):dict3.update(item)
print(dict3)