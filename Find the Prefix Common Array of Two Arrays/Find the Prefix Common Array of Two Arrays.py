class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        aSet = set()
        bSet = set()

        out = [0 for i in range(len(A))]

        for i in range(len(A)):
            aSet.add(A[i])
            bSet.add(B[i])

            out[i] = len(aSet.intersection(bSet))

        return out