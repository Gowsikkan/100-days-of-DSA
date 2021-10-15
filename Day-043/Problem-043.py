

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head):
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res == res[::-1]
    
if __name__ == '__main__':
 
    #Start with the empty list
    llist = Solution()
 
    llist.head = ListNode(1)
    llist.head.next = ListNode(1)
    llist.head.next.next = ListNode(3)
    llist.head.next.next.next = ListNode(4)

print(Solution().isPalindrome(llist.head))
