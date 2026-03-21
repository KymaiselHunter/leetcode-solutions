class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cons = 1

        for index, num in enumerate(flowerbed):
            # print(index, num, cons, cons//2)
            if not num:
                cons += 1
                if index == len(flowerbed)-1:
                    cons+=1

            if num or index == len(flowerbed)-1:
                n -= cons//2
                cons = 0

        return n <= 0
            
            