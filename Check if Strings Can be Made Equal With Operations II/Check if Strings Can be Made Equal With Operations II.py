class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        cEven = Counter(s1[0::2])
        cOdd = Counter(s1[1::2])

        # print(cEven)
        # print(cOdd)

        for index, char in enumerate(s2):
            c = cEven if index % 2 == 0 else cOdd 
            if char not in c: 
                return False

            if c[char] <= 0:
                return False

            c[char] -= 1
        
        # print(cEven)
        # print(cOdd)
        return True