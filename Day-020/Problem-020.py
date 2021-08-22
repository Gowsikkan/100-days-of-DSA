#Jewels and Stones

class Solution:
    def numJewelsInStones(self, jewels, stones):
        c=0
        for jewel in stones:
            if jewel in jewels:
                c += 1
        return c

s=input()
j=input()
print(Solution().numJewelsInStones(s,j))