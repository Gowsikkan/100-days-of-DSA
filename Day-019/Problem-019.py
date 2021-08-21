#Check if All Characters Have Equal Number of Occurrences

class Solution:
    def areOccurrencesEqual(self,s):
        for i in range(len(s)-1):
            if s.count(s[i])!=s.count(s[i+1]):
                return False
        return True

s=input()
print(Solution().areOccurrencesEqual(s))
