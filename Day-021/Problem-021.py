#Design a Stack With Increment Operation

class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize=maxSize
        self.stack=[]
        self.top=-1

    def push(self, x: int) -> None:
        if self.top!=self.maxSize-1:
            self.stack.append(x)
            self.top+=1

    def pop(self) -> int:
        if self.top!=-1:
            self.top-=1
            return self.stack.pop()
        return -1

    def increment(self, k: int, val: int) -> None:
        self.temp=0
        while self.temp<min(len(self.stack),k):
            self.stack[self.temp]+=val
            self.temp+=1

# Your CustomStack object will be instantiated and called as such:
maxSize=6
obj = CustomStack(maxSize)
obj.push(1)
obj.push(5)
obj.push(3)
print(obj.pop())
obj.push(4)

