#n=input('Enter the numbers you want to find:') #5
a=[3,0,1]
Sum=0
for i in a:
    Sum+=i
print("Actual sum is :",Sum)
Es=Sum*(Sum+1)//2
print('Expected sum is :',Es)
Missing_number_is=Es-Sum
print('Missing numner is :',Missing_number_is)
# f=n(n+1)/2
# S=sum(n)
# Difference_sum=f-S
# print(Difference_sum)
# Sum=0
# for val in a:
#     Sum+=val
# print(Sum)

