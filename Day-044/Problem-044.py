# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head,pos):
        curr=head
        c=0
        d=0
        while curr:
            if c==pos:
                d=curr
            if curr.next==d:
                return True
            curr=curr.next
            c=c+1
        return False
            
if __name__ == '__main__':
 
    #Start with the empty list
    llist = Solution()
 
    llist.head = ListNode(3)
    llist.head.next = ListNode(2)
    llist.head.next.next = ListNode(0)
    llist.head.next.next.next = ListNode(4)

n=1

print(Solution().hasCycle(llist.head,n))
