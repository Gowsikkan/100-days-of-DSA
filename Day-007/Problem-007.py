#Find the Highest Altitude

class Solution:
    def largestAltitude(self, gain):
        c=[0]
        for i in range(len(gain)):
            c.append(c[i]+gain[i])
        return max(c)

n = int(input())
c = []
for i in range(n):
    e = int(input())
    c.append(e)

print(Solution().largestAltitude(c))