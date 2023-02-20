##!usr/bin/env python3

#This is a single line comment
#python program to ilustrate the use of operators
#name: Lucy Sherkina
#Email:okwayosherkina@gmail.com
#Date:20th Feb 2023
#File:lists_revisit.py
'''append()-adds an element at the endof the lists
clear()-removes all items from a list
copy()-copies all elements into a second list
pop()-removes the element at the specified position
index()- Returns the index'''

fruits=["Banana", "Apple", "Mangoes", "Avocado","Orange"]

for fruit in fruits:
    print(fruit)

print(len(fruits))

friends=["Dion", "Nehemiah","Godwin", "Ida","Nyaga"]
print(friends)
friends[0]= "Bii"

new_friends=friends.copy()
print(new_friends)

new_friends.sort()
print(new_friends)
new_friends.pop()
print(new_friends)

new_friends.reverse()
print(new_friends)





