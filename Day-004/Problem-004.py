#Single Number

class Solution:
    def singleNumber(self,nums):
        for i in nums:
            if(nums.count(i)==1):
                return i

n = int(input("Enter size:"))
nums=[]
for i in range(n):
    e=int(input())
    nums.append(e)

print("Single number :",Solution().singleNumber(nums) )