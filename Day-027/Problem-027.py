#Build an Array With Stack Operations

class Solution:
    def buildArray(self,target,n):
        ans, j = [], 0
        for i in range(1,n+1):
            ans.append("Push")
            if target[j] == i:
                j += 1
            else:
                ans.append("Pop") 
            if j >= len(target):
                break
        return ans

s=int(input("Enter size"))
target = []
for i in range(s):
    w=int(input())
    target.append(w)

m=int(input("Enter no."))
print(Solution().buildArray(target,m))
