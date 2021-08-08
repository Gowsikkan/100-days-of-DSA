#Check If Two String Arrays are Equivalent

class Solution:
    def arrayStringsAreEqual(self, word1,word2):
        if "".join(word1)=="".join(word2):
            return True
        return False

n=int(input("Enter size :"))
c=[]
d=[]
print("List-1")
for i in range(n):
    c.append(input())
print("List-2")
for i in range(n):
    d.append(input())

print(Solution().arrayStringsAreEqual(c,d))
