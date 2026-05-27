class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        invalid = set()
        valid = set()

        left = set()

        for c in word:
            if c.lower() in invalid:
                continue
            if c.upper() in valid:
                if c.isupper():
                    continue
                valid.remove(c.upper())
                invalid.add(c)
                continue

            if c.lower() in left:
                if c.islower():
                    continue
                left.remove(c.lower())
                valid.add(c)
                continue

            if c.islower():
                left.add(c)
                continue
                
            invalid.add(c.lower())
            
        return len(valid)