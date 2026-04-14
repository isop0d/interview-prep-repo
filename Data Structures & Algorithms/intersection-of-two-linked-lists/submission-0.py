# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        n2 = headB
        n1 = headA
        n1len = 0
        n2len = 0

        while n1:
            n1len += 1
            n1 = n1.next
        while n2:
            n2len += 1
            n2 = n2.next

        n2 = headB
        n1 = headA
        
        if n1len < n2len:
            while n1len < n2len:
                n2 = n2.next
                n2len -= 1
        elif n1len > n2len:
            while n1len > n2len:
                n1 = n1.next
                n1len -= 1
        
        while n1 != n2:

            n1 = n1.next
            n2 = n2.next
        
        return n1
