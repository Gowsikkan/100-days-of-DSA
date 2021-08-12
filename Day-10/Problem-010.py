#Make Two Arrays Equal by Reversing Sub-arrays
class Solution:
    def canBeEqual(self,target,arr):
        if sorted(target) == sorted(arr):
            return True
        return False


target = [1,2,3,4] 
arr = [2,4,1,3]

print(Solution().canBeEqual(target,arr))