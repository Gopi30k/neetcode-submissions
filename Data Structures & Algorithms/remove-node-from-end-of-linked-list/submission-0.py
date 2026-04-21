# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = dummy

        # Phase 1: move fast n steps ahead
        for _ in range(n + 1):
            fast = fast.next

        # Phase 2: move both until fast.next is None
        while fast:
            slow = slow.next
            fast = fast.next

        # Delete the target node
        slow.next = slow.next.next
        return dummy.next