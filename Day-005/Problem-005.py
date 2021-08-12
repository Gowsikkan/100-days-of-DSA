#Count the Number of Consistent Strings

class Solution:
    def countConsistentStrings(self, allowed,words) -> int:
        c=0
        for i in words:
            for j in i:
                if j not in allowed:
                    c+=1
                    break
        return len(words)-c
    
n=int(input("Enter the size:"))
c=[]

for i in range(n):
    c.append(input())

allowed = input("Enter the string :")

print("Output : ",Solution().countConsistentStrings(allowed,c))