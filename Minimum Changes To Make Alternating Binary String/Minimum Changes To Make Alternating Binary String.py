class Solution:
    def minOperations(self, s: str) -> int:
        out = 0

        startOneInc = 0
        startZeroInc = 0
        for i in range(len(s)):
            if i%2==0:
                if s[i] == '1':
                    startZeroInc += 1

                if s[i] == '0':
                    startOneInc += 1
                continue
            
            if s[i] != '1':
                startZeroInc += 1

            if s[i] != '0':
                startOneInc += 1
                


        return min(startOneInc, startZeroInc)