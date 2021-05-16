'''
12. Write a Python program to remove a key from a dictionary.
'''

my_dict = {"ali":1,"veli":2,"isa":3,"musa":4}

key = input("Please enter a key : ")

del my_dict[key]

print(my_dict)