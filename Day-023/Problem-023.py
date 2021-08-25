#Maximum Nesting Depth of the Parentheses

class Solution:
    def maxDepth(self, s):
        count=0
        max_count=0
        for c in s:
            if c == '(':
                count += 1
                max_count = max(max_count, count)
            elif c == ')':
                count -= 1
        return max_count

s=input("Enter string :")
print(Solution().maxDepth(s))
