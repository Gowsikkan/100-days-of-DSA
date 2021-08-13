#Defanging an IP Address

class Solution:
    def defangIPaddr(self,address):
        s=""
        for i in address:
            if i==".":
                s+="[.]"
            else:
                s+=i
        return s

n = input("Enter string :")

print(Solution().defangIPaddr(n))