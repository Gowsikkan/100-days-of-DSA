#Convert Binary Number in a Linked List to Integer


# Definition for singly-linked list.

class Solution:
    def getDecimalValue(self, head):
        lst = []
        temp=head
        while temp:
            lst.append(str(temp.val))
            temp=temp.next
        s="".join(lst)
        ans=int(s,2)
        return ans
        
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

if __name__ == '__main__':
 
    #Start with the empty list
    llist = Solution()
 
    llist.head = ListNode(1)
    llist.head.next = ListNode(2)
    llist.head.next.next = ListNode(3)
    llist.head.next.next.next = ListNode(4)
    llist.head.next.next.next.next = ListNode(5)
    

print(Solution().getDecimalValue(llist.head))