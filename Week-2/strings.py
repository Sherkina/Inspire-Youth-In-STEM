#!usr/bin/env python3

#This is a single line comment
#python program to ilustrate the use of operators
#name: Lucy Sherkina
#Email:okwayosherkina@gmail.com
#Date:17th Feb 2023
#File:strings.py

poem= """This is a poem about nothing:
         Its funny people laugh about nothing"""

print(poem)
print(len(poem))

f_name= "Lucy"
s_name= "Sherkina"
full_name=f_name + s_name

age=25

print("My name is" + "and I am" + str(age) + "years old")

print("my name is {} and I am {} years old".format(full_name,age))