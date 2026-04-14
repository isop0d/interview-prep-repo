class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupprev = dummy

        while True:
            kthnode = self.travelKnodes(groupprev, k)
            if not kthnode:
                break
            next_group = kthnode.next
            curr = groupprev.next
            prev = next_group
            while curr != next_group:
                next = curr.next
                curr.next = prev
                prev = curr 
                curr = next
            tmp = groupprev.next
            groupprev.next = kthnode
            groupprev = tmp
        return dummy.next




    def travelKnodes(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr 