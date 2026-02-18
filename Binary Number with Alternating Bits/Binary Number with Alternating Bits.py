class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        odd = n % 2 
        while n > 0:
            curr = n % 2 
            if odd and not curr:
                return False
            if not odd and curr:
                return False
            # print(n, curr)
            n //= 2
            odd = not odd
        return True
