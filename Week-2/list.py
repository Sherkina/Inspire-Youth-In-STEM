names = ["Chris", "Jamil", "Lynn", "Lewis", "Mkamburi", "Kirui"]
#Accessing items on a list

print(names)
print(names[0])
print(names[-1])
print(names[0:3])
fruits=["Mango","Oranges","Watermelon","passion","bananas","Guavas","Apples"]
print(fruits[0:-1])
print(fruits[5])
print("My favorite fruit is:", (fruits[3].upper()))
vegetables=["kales","cabbage","spinnach","managu","Brocoli"]
stationery=["pens","pencils","ink","paper","pouch","scissors","stapler"]
shoppings=vegetables + stationery
print(shoppings)
print(shoppings[5])
for vegetable in vegetables:
    print(vegetable)
for shopping in shoppings:
    print(shopping)
print("My name is " + names[3]+ " and my favorite fruit is " +fruits[3])
