list=[]
num=int(input("Enter the first number :"))
list.append(num)
num=int(input("Enter the second number :"))
list.append(num)
num=int(input("Enter the third number :"))
list.append(num)
num=int(input("Enter the fourth number :"))
list.append(num)
num=int(input("Enter the fifth number :"))
list.append(num)
list.sort()
print(list)
totalsum=sum(list)
print(totalsum)
avg=totalsum/5
print(avg)
print(len(list))
maxterm=max(list)
print("maximium number is ",maxterm)
minterm=min(list)
print("mininium number is",minterm)


