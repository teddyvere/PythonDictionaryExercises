'''
11. Write a Python program to multiply all the items in a dictionary

'''

my_dict = {'data1':5,'data2':-5,'data3':3}

total = 1

for key,value in my_dict.items():
    total *= value

print(total)