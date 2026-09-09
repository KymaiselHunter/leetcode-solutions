class Solution:
    def countCommas(self, n: int) -> int:
        out = 0
        it = 0
        hold = 0
        sub = 1
        while n:
            curr = n % 1000
            n //= 1000

            if not n:
                break

            hold += curr * pow(10,it)
            out += (pow(10,it+3) * ((n % 1000)-sub)) + (hold+1)
            # print(curr, out)
            # print(pow(10,it+3), n, ((n % 1000)-1))
            sub = 0

            # (pow(10,it+3) * ((n % 1000) - 1)) + (small + 1)
            it += 3

        return out

