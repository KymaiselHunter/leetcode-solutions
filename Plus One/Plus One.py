class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        
        for i in range(len(digits)-1,-1,-1):
            inc = digits[i] + carry
            carry = inc // 10
            digits[i] = inc % 10

            if carry == 0:
                return digits

        if carry != 0:
            digits.insert(0, carry)

        return digits