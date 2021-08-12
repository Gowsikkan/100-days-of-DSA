#Find N Unique Integers Sum up to Zero

class Solution:
    def sumZero(self, n: int):
        c=[]
        for i in range(1,n):
            c.append(i)
        c.append(-sum(c))
        return c

n=int(input())

print(Solution().sumZero(n))
