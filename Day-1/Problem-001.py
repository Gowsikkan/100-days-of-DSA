#Create Target Array in the Given Order

class Solution:
    def createTargetArray(self,nums,index):
        s=[]
        for i in range(len(nums)):
            s.insert(index[i],nums[i])
        return s
    

n=int(input("Enter size : "))

nums = []
index = []

for i in range(n):
    c=int(input("Enter values :"))
    nums.append(c)

for i in range(n):
    c=int(input("Enter index :"))
    index.append(c)

print(Solution().createTargetArray(nums,index))

