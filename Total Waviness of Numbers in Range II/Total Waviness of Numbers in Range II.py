class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        dp = dict()
        out = 0

        def recur(num: int):
            if num < 100:
                dp[num] = 0
                return 0
            
            if num in dp:
                return dp[num]

            increment = 0
            increment += recur(num // 10)

            right = num % 10
            mid = (num // 10) % 10
            left = (num // 100) % 10

            if left < mid and mid > right:
                increment += 1
            elif left > mid and mid < right:
                increment += 1

            dp[num] = increment
            return increment

        for i in range(num1, num2+1):
            out += recur(i)

        return out