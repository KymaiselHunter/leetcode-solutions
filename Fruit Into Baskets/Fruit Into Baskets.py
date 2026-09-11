class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        d = dict()
        out = 0

        # right to left
        for i in range(len(fruits)-1,-1,-1):
            # get curr fruit 
            currFruit = fruits[i]

            # keep track of fruits in current
            # left value will be count, right value will be left most occurence
            if currFruit not in d:
                d[currFruit] = (1, i)
            else:
                d[currFruit] = (d[currFruit][0] + 1, i)

            # if there's more than two fruits, remove
            if len(d) > 2:
                # if there's more than two fruits, remove the third
                rightFruit = max(d.items(), key=lambda item: item[1][1])[0]
                # print(d.items())
                # print(rightFruit)
                d.pop(rightFruit)

                # update the fruit that wasnt removed
                for key in d.keys():
                    if key == currFruit:
                        continue
                    d[key] = (d[key][1] - i, d[key][1])
            
            # if there's only two fruits, we should add up
            out = max(out, sum(k[0] for k in d.values()))
            print(out, d)

        return out