#Baseball Game

class Solution:
    def calPoints(self, ops):
        s=[]
        c=-1
        for i in ops:
            if i =="D":
                s.append(s[c]*2)
                c+=1
            elif i=="C":
                s.pop()
                c-=1
            elif i=="+":
                s.append(s[c]+s[c-1])
                c+=1
            else:
                s.append(int(i))
                c+=1
        return sum(s)

n=int(input("Enter size : "))
s=[]
for i in range(n):
    s.append(input())

print("Sum :",Solution().calPoints(s))
