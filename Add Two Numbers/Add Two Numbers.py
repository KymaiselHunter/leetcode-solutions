# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cache = l2
        output = l1
        prevL1 = None
        prevL2 = None

        carry = 0
        while l1 and l2:
            sum = l1.val + l2.val + carry
            l1.val = sum % 10 
            carry = sum // 10

            prevL1 = l1
            l1 = l1.next

            prevL2 = l2
            prevL2.val = 0
            l2 = l2.next

        if not l1:
            prevL1.next = l2
            l1 = l2
            prevL2.next = None

        while carry > 0:
            if not l1:
                prevL1.next = cache
                l1 = cache
                cache = cache.next
                l1.next = None
            # print(l1)
            sum = l1.val + carry
            l1.val = sum % 10 
            carry = sum // 10
            # print(sum, carry)
            prevL1 = l1
            l1 = l1.next


        return output