# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
#
#   1 -> 2 -> 3 -> Null
#   ^    ^
#p  c    n
# <-1    2 -> 3 -> Null
#   ^    ^
#p  c    n
# <-1    2 -> 3 -> Null
#   ^    ^    ^
#   p    c    n
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr 
            curr = next
        return prev

