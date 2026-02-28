class Solution:
    def concatenatedBinary(self, n: int) -> int:
        output = str()

        for i in range(1,n+1):
            output += str(bin(i)[2:])

        return int(output,2) % (pow(10,9) + 7)
