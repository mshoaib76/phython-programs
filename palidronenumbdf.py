
list=[]
for i in range(0,4):

    number = int(input("enter the numner "))
    list.append(number)

# list=[1,2,1]
# list2=[1,2,3,4,5]
    copylist=list.copy()
    copylist.reverse()

if(copylist==list):
    print("plandrone number")
else:
    print("nor plandrone number")