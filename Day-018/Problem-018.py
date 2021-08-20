 #Merge Strings Alternately

class Solution:
    def mergeAlternately(self, word1,word2):
        c=[]
        for i in range(max(len(word1),len(word2))):
            if i <len(word1):
                c.append(word1[i])
            if i<len(word2):
                c.append(word2[i])
        return "".join(c)
    
word1=input("Enter string1:")
word2=input("Enter string2:")
print(Solution().mergeAlternately(word1,word2))