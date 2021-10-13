# Remove Duplicates from Sorted List


# Definition for singly-linked list.

class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head):
        curr = head
        while curr:
            if curr.next and curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head


if __name__ == '__main__':
 
    #Start with the empty list
    llist = Solution()
 
    llist.head = ListNode(1)
    llist.head.next = ListNode(1)
    llist.head.next.next = ListNode(3)
    llist.head.next.next.next = ListNode(4)

c=Solution().deleteDuplicates(llist.head)
print(c.val,c.next.val,c.next.next.val)