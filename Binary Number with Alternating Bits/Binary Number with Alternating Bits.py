class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        odd = True
        while n:
            curr = n % 2 
            if odd and not curr:
                return False
            if not odd and curr:
                return False
            n //= 2
            odd = not odd
        return True
