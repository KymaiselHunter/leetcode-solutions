class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = Counter(arr)

        vals = list(c.values())
        uniques = set(vals)

        return len(vals) == len(uniques)
        # print(list(c.values()))
        # print(set(list(c.values())))

