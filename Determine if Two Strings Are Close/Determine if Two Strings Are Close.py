class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1 = Counter(word1)
        c2 = Counter(word2)

        vals1 = sorted(list(c1.values()))
        vals2 = sorted(list(c2.values()))

        chars1 = set(word1)
        chars2 = set(word2)

        return vals1 == vals2 and chars1 == chars2 
        # print(vals1)
        # print(vals2)