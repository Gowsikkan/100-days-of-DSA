#Maximum Number of Words You Can Type

class Solution:
    def canBeTypedWords(self, text, brokenLetters):
        c=[]
        d=0
        c=text.split()
        for i in c:
            for j in i:
                if j in brokenLetters:
                    d=d+1
                    break
        return len(c)-d
                

text=input("Enter String :")
BrokenLetters = input("Enter String :")

print(Solution().canBeTypedWords(text,BrokenLetters))