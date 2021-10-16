# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head,pos):
        curr=head
        c=[]
        while curr:
            if curr.next in c:
                return True
            else:
                c.append(curr)
                curr=curr.next
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
