'''
10. Write a Python program to sum all the items in a dictionary. 
'''

dict1 = {1:5,2:4,3:6,4:8,5:12}

sum1 = 0

for key,value in dict1.items():
    sum1 += value

print(sum1)

################################################################################################################

my_dict = {'data1':100,'data2':-54,'data3':247}
print(sum(my_dict.values()))