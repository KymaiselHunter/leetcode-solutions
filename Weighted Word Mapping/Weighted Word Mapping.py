class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        out = []

        for word in words:
            curr = 0
            for letter in word:
                curr += weights[ord(letter) - ord('a')]
            out.append(chr(ord('z') - (curr % 26)))

        return "".join(out)