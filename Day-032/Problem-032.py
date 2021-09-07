#First Unique Character in a String

class Solution:
    def firstUniqChar(self,s):
        for i in list(dict.fromkeys(s)):
            if s.count(i) == 1:
                return s.index(i)
        return -1
        

s=input()
print(Solution().firstUniqChar(s))