class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 2:
            return n
        if n == 2:
            return 1

        prevOne = 0
        prevTwo = 1
        prevThree = 1

        for i in range(n-2):
            curr = prevThree + prevTwo + prevOne

            prevThree, prevTwo, prevOne = curr, prevThree, prevTwo

        return prevThree
