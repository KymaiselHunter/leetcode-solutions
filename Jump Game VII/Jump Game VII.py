class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == '1':
            return False

        dp = [None for i in range(len(s))]

        def recur(index):
            # print(index)
            if index >= len(s):
                return False
            if s[index] == '1':
                dp[index] = False
                return False
            if index == len(s)-1:
                dp[index] = True
                return True
            if dp[index] is not None:
                return dp[index]

            for i in range(
                index + minJump, 
                min(index + maxJump + 1, len(s))
            ):
                if recur(i):
                    dp[index] = True
                    return True
            dp[index] = False
            return False
            
        return recur(0)