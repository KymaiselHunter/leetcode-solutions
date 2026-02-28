class Solution:
    def concatenatedBinary(self, n: int) -> int:
        output = int()
        bits = 1

        for i in range(1,n+1):
            if pow(2, bits) <= i:
                bits  += 1

            output = output << bits
            output = output | i

        return output % (pow(10,9) + 7)
