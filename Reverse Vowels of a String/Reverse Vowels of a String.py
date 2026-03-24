class Solution:
    def reverseVowels(self, s: str) -> str:
        cStack = list()
        vStack = list()
        vowels = {'a' , 'e', 'i', 'o', 'u'}

        for index, letter in enumerate(s):
            if letter.lower() in vowels:
                vStack.append(letter)
                continue
            cStack.append(letter)

        out = list()
        
        for letter in s:
            if not cStack:
                out += vStack[::-1]
                break
            if not vStack:
                out += cStack
                break
            if letter != cStack[0]:
                out.append(vStack[-1])
                vStack.pop(-1)
                continue
            out.append(cStack[0])
            cStack.pop(0)

        return "".join(out)
