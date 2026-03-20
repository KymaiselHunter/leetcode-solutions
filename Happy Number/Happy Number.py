class Solution:
    def isHappy(self, n: int) -> bool:
        cache = set()

        while True:
            # print(n, cache)
            if n in cache:
                return False
            
            cache.add(n)

            curr = n
            check = 0

            while curr:
                check += pow(curr % 10, 2)
                curr //= 10
            n = check
            if check == 1:
                return True
            