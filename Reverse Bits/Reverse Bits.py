class Solution:
    def reverseBits(self, n: int) -> int:
        hold = []
        while n:
            hold.insert(0,n%2)
            n //= 2

        while len(hold) < 32:
            hold.insert(0,n%2)

        out = 0

        # print(hold)

        for i in range(len(hold)):
            if hold[i]:
                out += pow(2, i)

        return out