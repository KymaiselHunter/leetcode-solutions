# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        if not head.next:
            return None
        
        prev = head
        slow = head
        fast = head

        while slow and fast and fast.next:
            # print(slow.val, fast.val)
            prev = slow
            slow = slow.next
            fast = fast.next
            
            if fast:
                fast = fast.next

        # print(slow.val, slow)
        prev.next = slow.next

        return head