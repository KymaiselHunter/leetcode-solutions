class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        d = dict()
        out = 0

        # right to left
        for i in range(len(fruits)-1,-1,-1):
            # get curr fruit 
            currFruit = d[i]

            # keep track of fruits in current
            # left value will be count, right value will be left most occurence
            if currFruit not in d:
                d[currFruit] = (1, i)
            else:
                d[currFruit] = (d[currFruit][0] + 1, i)

            # if there's only two fruits, we should add up