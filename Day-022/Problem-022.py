#Min Stack

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.S = [] #for your stack
        self.M = [] #for storing the min value till the respective idx

    def push(self, val: int) -> None:
        self.S.append(val)
        M = self.M
        M.append(val if not M else min(val,M[-1]))
        
    def pop(self) -> None:
        self.S.pop()
        self.M.pop()

    def top(self) -> int:
        return self.S[-1]

    def getMin(self) -> int:
        return self.M[-1]
        
        

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
obj.pop()
obj.push(5)
print(obj.top())
print(obj.getMin())