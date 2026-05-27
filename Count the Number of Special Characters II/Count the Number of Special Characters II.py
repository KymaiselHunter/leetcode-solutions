class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        invalid = set()
        valid = set()

        left = set()

        for c in word:
            # print(c)
            # print(valid)
            # print(invalid)
            # print(left)
            if c.lower() in invalid:
                continue
            if c.upper() in valid and c.islower():
                valid.remove(c.upper())
                invalid.add(c)
                print(valid)
                continue

            if c.lower() in left and c.isupper():
                left.remove(c.lower())
                valid.add(c)
                continue

            if c.islower():
                left.add(c)
                continue
            if c.lower() not in left and c.upper() not in valid:
                invalid.add(c.lower())
        # print(valid)
        return len(valid)