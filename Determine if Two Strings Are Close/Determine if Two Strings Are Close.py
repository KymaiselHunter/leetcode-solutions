class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1 = Counter(word1)
        c2 = Counter(word2)

        vals1 = set(list(c1.values()))
        vals2 = set(list(c2.values()))

        return vals1 == vals2
        # print(vals1)
        # print(vals2)