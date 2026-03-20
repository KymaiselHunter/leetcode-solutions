class Solution:
    def addDigits(self, num: int) -> int:
        currNum = num
        while currNum > 10:
            # print(currNum)
            nextNum = 0

            while currNum:
                nextNum += currNum % 10
                currNum //= 10

            currNum = nextNum

        return currNum


