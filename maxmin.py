list=[]
num=int(input("Enter the first numner :"))
list.append(num)
num=int(input("Enter the second numner :"))
list.append(num)
num=int(input("Enter the third numner :"))
list.append(num)
num=int(input("Enter the fourth numner :"))
list.append(num)
num=int(input("Enter the fifth numner :"))
list.append(num)
list.sort()
print(list)
# list.max()
# print(list)
# list.min()
# print(list)
sum=list[0]+list[1]+list[2]+list[3]+list[4]
print(sum)
avg=sum/5
print(avg)


