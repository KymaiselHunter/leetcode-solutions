class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        cache = set()
        out = set()

        for char in word:
            cache.add(char)

            if char.upper() in cache and char.lower() in cache:
                out.add(char.lower())

        return len(out)