class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        dp = dict()
        out = 0

        for i in range(num1, num2+1):
            curr = i
            increment = 0
            while curr >= 100:
                if curr in dp:
                    increment += dp[curr]
                    break

                right = curr % 10
                mid = (curr // 10) % 10
                left = (curr // 100) % 10

                curr //= 10

                if left < mid and mid > right:
                    increment += 1
                    continue

                if left > mid and mid < right:
                    increment += 1

            dp[i] = increment
            out += increment

        return out