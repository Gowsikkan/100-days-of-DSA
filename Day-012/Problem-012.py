#Valid Anagram

class Solution:
    def isAnagram(self, s,t):
        if "".join(sorted(s))=="".join(sorted(t)):
            return True
        return False
    
n=input("Enter string-1 : ")
t=input("Enter string-2 : ")
print(Solution().isAnagram(n,t))