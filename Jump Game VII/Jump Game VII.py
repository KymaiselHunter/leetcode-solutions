class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == '1':
            return False

        jumpList = [False for i in range(len(s))]
        jumpList[0] = True
        counter = 0

        for i in range(1, len(s)):
            smallJump = i - minJump
            if smallJump >= 0:
                counter += jumpList[smallJump]
            
            bigJump = i - maxJump - 1

            if bigJump >= 0:
                counter -= jumpList[bigJump]

            jumpList[i] = counter > 0 and s[i] == '0'

        return jumpList[-1]