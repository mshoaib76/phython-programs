final_result=[]
nums=[1,2,3,4]
s=nums[-1]
result=1
#step1
for i in nums:
 result*=i
final_result.append(result)
#step2
for j in range(len(nums)-2,-1,-1):
 final_result.append(s*nums[j])
#result
print(final_result)


