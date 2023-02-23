#advanced data types
#mutable vs immutable
#mutable are datatypes that can changeduring the life cycle of the program i
#immutable are data types that cannot be edited during the life cycle of the program
#ble vs immutable


#1) Lists(mutable,immutable)
#3)dictionaries aka dict
#4)sets

'''friends=["Nehemiah", "Mwanyalo", "Godwin", "mkamburi"]
#or []for an empty list
#addelements......Append(), extend()
students=["Nehemiah", "Mwanyalo", "Godwin", "mkamburi"]
friends.extend(students)
print(friends)
friends.append("Lucy")
print(friends)

friends.sort()
print(friends)

#Tuples-------unchangeable lists

stationeries=("pens","pencils","books")
for stationery in stationeries:
    print(stationery)

numbers  (1,2,3,4,5,6,7,86,96)'''

#Dictionaries aka dict

#uses key and value pair

student={"name":"Lucy","age":"17","gender":"female","is_tall":True}
print(student["name"])
print(student["age"])
print(student["gender"])
print(student["is_tall"])

friend= {"fav_color":"burgundy","hobby":"dancing","course":"nursing"}
print(friend["fav_color"])
print(friend["hobby"])
print(friend["course"])
