# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: reverse second half
        second = slow.next
        slow.next = None        # cut the list
        prev = None
        curr = second
        while curr:
            temp     = curr.next
            curr.next = prev
            prev     = curr
            curr     = temp
        second = prev           # new head of reversed half

        # Step 3: weave
        l1, l2 = head, second
        while l2:
            next1 = l1.next
            next2 = l2.next
            l1.next = l2
            l2.next = next1
            l1 = next1
            l2 = next2