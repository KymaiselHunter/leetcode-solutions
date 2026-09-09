class Solution:
    def countCommas(self, n: int) -> int:
        out = 0
        it = 0

        while n:
            curr = n % 1000
            n //= 1000

            if not n:
                break

            out += (pow(10,it+3) * ((n % 1000)-1)) + (pow(10,it) * curr+1)  

        return out

