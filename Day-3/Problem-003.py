#Kids With the Greatest Number of Candies

class Solution:
    def kidsWithCandies(self, candies,extraCandies):
        c=list()
        for i in candies:
            if i+extraCandies>=max(candies):
                c.append(True)
            else:
                c.append(False)
        return c

candies =[]
n=int(input("Enter size :"))

for i in range(n):
    e=int(input())
    candies.append(e)

extraCandies = int(input("Extra Candies : "))

print(Solution().kidsWithCandies(candies,extraCandies))

                