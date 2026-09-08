class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pCount  = Counter(p)
        currCount = Counter()
        left = 0
        out = list()

        for i, c in enumerate(s):
            # print(pCount, currCount)
            if currCount[c] < pCount[c]:
                if c in currCount: 
                    currCount[c] += 1
                else:
                    currCount[c] = 1
                
                if currCount == pCount:
                    out.append(left)
                continue

            while currCount[c] >= pCount[c]:
                currCount[s[left]] -= 1
                left += 1

            currCount[c] += 1
            if currCount == pCount:
                    # print(i, left)
                    out.append(left)

        return out
