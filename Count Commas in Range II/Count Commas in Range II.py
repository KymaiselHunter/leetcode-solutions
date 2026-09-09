class Solution:
    def countCommas(self, n: int) -> int:
        it = 0
        out = 0
        mult = 999

        while n:
            if mult >= n:
                out += n * it
                break
            
            out += mult * it
            n-=mult
            mult *= 1000
            it += 1


        return out

