#Remove Outermost Parentheses

class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        count=0
        ans=[]
        
        for i in S:
            if i=="(":
                if count!=0:
                    ans.append(i)
                count+=1
            else:
                if count!=1:
                    ans.append(i)
                count -= 1
               
        return "".join(ans)

s=input("Enter string: ")
print(Solution().removeOuterParentheses(s))