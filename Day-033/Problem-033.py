#Implement Queue using Stacks

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack=[]
        
    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.stack.pop(0)
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.stack[0]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.stack)==0


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
print(obj.pop())
print(obj.peek())
print(obj.empty())
