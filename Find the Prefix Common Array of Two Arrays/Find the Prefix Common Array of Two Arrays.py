class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        freq = [0 for i in range(len(A))]
        out = [0 for i in range(len(A))]
        prev = 0

        for i in range(len(A)):
            if A[i] == B[i]:
                out[i] = prev + 1
                prev = out[i]
                freq[i-1] += 2
                continue

            freq[A[i]-1] += 1
            freq[B[i]-1] += 1

            if freq[A[i]-1] >= 2:
                out[i] += 1
            if freq[B[i]-1] >= 2:
                out[i] += 1

            out[i] += prev
            prev = out[i]

        return out