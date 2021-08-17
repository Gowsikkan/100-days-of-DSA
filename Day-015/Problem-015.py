#Valid Palindrome

class Solution:
    def isPalindrome(self,s):
        c=0
        d=''.join(e for e in s if e.isalnum())
        d=d.lower()
        for i in range(len(d)):
            c=c-1
            if d[i]!=d[c]:
                return False
        return True
    
s=input("Enter String:")
print(Solution().isPalindrome(s))
                
                