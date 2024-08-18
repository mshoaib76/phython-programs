"""name check ends words that is same or not is your given words is same than
its print true otherwise false..... in second concept i also add two string and also check
their length and than print their sum of length"""


name=input("enter name:")
print(name)
print(name.endswith("och"))
name2=input("enter another name:")
print(name2)
print(name2.endswith("eed"))
#words count ...how much time word is repeat
print(name.count("a"))



total=name+name2
print(total)
print(len(name))
print(len(name2))
print(len(total))
#in this line ......it's capitilze first word
name3=name.capitalize()
print(name3)
#replacing words by useing this concept
print(name.replace("o","s"))
#find any keyword of index by using find keyword
print(name2.find("e"))
