#Valid Parentheses

class Solution:
    def isValid(self, s):
        c=[]
        v=-1
        for i in s:
            if i=='('or i=='['or i=='{':
                c.append(i)
                v+=1
            else:
                if v==-1:
                    return False
                elif c[v]=='(' and i==')' or c[v]=='[' and i==']' or c[v]=='{' and i=='}':
                    c.pop()
                    v-=1
                else:
                    return False
        return True if v==-1 else False

s=input()
print(Solution().isValid(s))