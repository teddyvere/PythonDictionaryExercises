'''
4. Write a Python script to check whether a given key already exists in a dictionary.
'''
dict1 = {1:5,2:4,3:10,4:20,5:1}

key = int(input("Please enter a key : "))

if key in dict1:
    print("Yes")
else:
    print("No")