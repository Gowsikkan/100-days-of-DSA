

class Solution:
     def nextGreaterElement(self, nums1, nums2):
        if not nums1 or not nums2:
            return []
        d={}
        stack=[nums2[0]]
        for i in range(1,len(nums2)):
            while(stack and nums2[i]>stack[-1]):
                d[stack.pop()]=nums2[i]
            stack.append(nums2[i])
        for j in stack:
            d[j]=-1
        return [d[j] for j in nums1] 

s1=[]
s2=[]

n1=int(input("Enter size-1"))
for i in range(n1):
    e=int(input())
    s1.append(e)

n2=int(input("Enter size-2"))
for j in range(n2):
    r=int(input())
    s2.append(r)

print(Solution().nextGreaterElement(s1,s2))