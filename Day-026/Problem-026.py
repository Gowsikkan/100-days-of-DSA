#Final Prices With a Special Discount in a Shop

class Solution:
    def finalPrices(self, prices):
        final=[]
        for i in range(len(prices)-1):
            status= False
            
            for j in range(i+1,len(prices)):
                if prices[i] >= prices[j]:
                    final.append(prices[i]-prices[j])
                    status = True
                    break
            if status == False:
                final.append(prices[i])
    
        final.append(prices[-1])  
        return(final)

n=int(input())
c=[]
for i in range(n):
    e=int(input())
    c.append(e)

print(Solution().finalPrices(c))