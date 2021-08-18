#Uncommon Words from Two Sentences

class Solution:
    def uncommonFromSentences(self,s1,s2):
        c=[]
        text = s1 + " " + s2
        for i in text.split():
            if text.split().count(i)==1:
                c.append(i)
        return c

s1=input("Enter String :")
s2=input("Enter String :")

print(Solution().uncommonFromSentences(s1,s2))