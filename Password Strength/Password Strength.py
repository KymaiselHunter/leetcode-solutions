class Solution:
    def passwordStrength(self, password: str) -> int:
        c = set()
        out = 0
        sp = {'!', '@', '#', "$"}
        
        for char in password:
            if char in c:
                continue

            c.add(char)

            if char in sp:
                out += 5
                continue

            if char.isdigit():
                out += 3
                continue

            if char.isalpha():
                if char.isupper():
                    out += 2
                    continue
                out += 1

        return out

                