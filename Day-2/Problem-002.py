 #Maximum Product Difference Between Two Pairs

class Solution:
    def maxProductDifference(self,nums):
        nums.sort()
        return (nums[len(nums)-1]*nums[len(nums)-2])-(nums[0]*nums[1])


n=int(input("Enter length of List :"))
e=[]
print("Enter values")
for i in range(n):
    s=int(input())
    e.append(s)

print(Solution().maxProductDifference(e))
