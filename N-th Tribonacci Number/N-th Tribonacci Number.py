class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 3:
            return n

        prevOne = 0
        prevTwo = 1
        prevThree = 1

        for i in range(n-2):
            curr = prevThree + prevTwo + prevOne

            prevThree, prevTwo, prevOne = curr, prevThree, prevTwo

        return prevThree
