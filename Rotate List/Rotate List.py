# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        length = 0
        it = head
        while it:
            length += 1
            it = it.next

        rotate = k % length
        if rotate == 0:
            return head

        it = head
        prev = None

        for i in range(length - rotate):
            prev = it
            it = it.next
        prev.next = None
        
        out = it

        while it.next:
            it = it.next

        it.next = head
        return out