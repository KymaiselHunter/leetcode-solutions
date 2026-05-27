class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        invalid = set()
        valid = set()

        left = set()

        for c in word:
            if c.lower() in invalid:
                continue

            if c.upper() in valid and c.islower():
                valid.remove(c.upper())
                invalid.add(c)
                continue

            if c.lower() in left and c.isupper():
                left.remove(c.lower())
                valid.add(c)
                continue

            if c.islower():
                left.add(c)
            else:
                invalid.add(c.lower())
        
        return len(valid)