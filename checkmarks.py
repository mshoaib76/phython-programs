name=input("enter your name:")

marks =int(input("enter your marks"))
print(name)
if(marks>=90):
    print("Grade A")
elif(marks>=70 & marks<89):
    print("Grade B")
elif(marks>=50 & marks<69):
    print("Grade C")
else:
    print("Grade F")
