# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        p = head
        n = head.next

        evenHead = head.next
        evenIt = None

        while p and n:
            # print(p.val)
            if not evenIt:
                evenIt = n
            else:
                evenIt.next = n
                evenIt = n

            p.next = n.next
            n = p.next
            if n:
                p = p.next
                n = n.next

        evenIt.next = None
        p.next = evenHead

        return head 
        



        