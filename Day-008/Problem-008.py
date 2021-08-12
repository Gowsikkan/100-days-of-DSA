#Number Of Rectangles That Can Form The Largest Square

class Solution:
    def countGoodRectangles(self, rectangles) -> int:
        c=[]
        for i in rectangles:
            c.append(min(i))
        return c.count(max(c))

rectangles = [[5,8],[3,9],[5,12],[16,5]]
print(Solution().countGoodRectangles(rectangles))