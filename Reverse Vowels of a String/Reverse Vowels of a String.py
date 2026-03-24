class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a' , 'e', 'i', 'o', 'u'}
        left = 0
        right = len(s)-1
        
        out = list(s)

        while left < right:
            if out[left].lower() in vowels and out[right].lower() in vowels:
                out[left], out[right] = out[right], out[left]
                left += 1
                right -= 1
                continue

            if not out[left].lower() in vowels:
                left += 1
            if not out[right].lower() in vowels:
                right -= 1

        return "".join(out)

