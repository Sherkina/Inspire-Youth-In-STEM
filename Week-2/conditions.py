age =16

gender="female"


if(age<18):
    print("You are still young")
else:
    print(" You should get an id")

#compund/multiple conditions


if((age >30) & (gender == 'female')):
    print("You qualify for a loan")
else:
    print("No loan foryou")

fav_color ="gray"
age =22
if(fav_color == "gray") | (age<=20)):
    print("Happy birthday to you")
else:
    print("No birthday present for you")