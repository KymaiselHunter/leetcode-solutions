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
        
        slow = None
        fast = head

        while fast and fast.next:
            # print(slow.val, fast.val)
            if not slow:
                slow = head
            else:
                slow = slow.next
            fast = fast.next
            
            if fast:
                fast = fast.next

        # print(slow.val, slow)
        slow.next = slow.next.next

        return head