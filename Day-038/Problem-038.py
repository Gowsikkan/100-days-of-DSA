#Middle of the Linked List

# Definition for singly-linked list.

class Solution:
    def middleNode(self, head):
        temp=head
        e=0
        while temp:
            e+=1
            temp=temp.next
        mid=e//2
        c=0
        newtemp=head
        while newtemp:
            if mid==c:
                s=newtemp
            newtemp=newtemp.next
            c+=1
        while s:
            print(s.val)
            s=s.next
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
    

c=Solution().middleNode(llist.head)
