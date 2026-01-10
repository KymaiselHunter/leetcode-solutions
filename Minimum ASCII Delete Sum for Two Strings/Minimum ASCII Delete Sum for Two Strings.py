class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        def stringToValue(s: str):
            output = 0
            for letter in s:
                output += ord(letter)

            return output

        cache = [[0 for j in range(len(s2)+1)] for i in range(len(s1)+1)]
        
        for i in range(len(s1)-1,-1,-1):
            for j in range(len(s2)-1,-1,-1):
                print(i,j)
                if s1[i] == s2[j]:
                    cache[i][j] = ord(s1[i]) + cache[i+1][j+1]
                    continue

                cache[i][j] = max(cache[i+1][j], cache[i][j+1])
        # print(cache[0][0])
        # print(cache)

        return stringToValue(s1) + stringToValue(s2) - cache[0][0]*2


                

                

        