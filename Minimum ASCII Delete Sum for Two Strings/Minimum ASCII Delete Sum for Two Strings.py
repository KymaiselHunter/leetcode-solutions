class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        def stringToValue(s: str):
            output = 0
            for letter in s:
                output += ord(letter)

            return output


        # def normalize(normal: str, compare: str) -> str:
        #     output = str()
        #     for letter in normal:
        #         if letter in compare:
        #             output += letter
        #     return output

        # n1 = normalize(s1, s2)
        # n2 = normalize(s2, n1)

        # print(n1, n2)
        cache = dict()
        def dp(i: int, j: int) -> int:
            # print(i, len(s1), j, len(s2))
            if i >= len(s1) or j >= len(s2):
                return 0

            if tuple(sorted({s1[i:], s2[j:]})) in cache:
                # print(cache[tuple(sorted({s1[i:], s2[j:]}))])
                return cache[tuple(sorted({s1[i:], s2[j:]}))]
            o1=dp(i+1, j)
            o2=dp(i, j+1)
            
            output = o2
            # print(o1,o2)
            if o1 > o2:
                output = o1

            if s1[i] == s2[j]:
                # cache.add(s1[i] + dp(i+1, j+1))
                output = ord(s1[i]) + dp(i+1, j+1)
            # print(output)
            cache[tuple(sorted({s1[i:], s2[j:]}))] = output
            return output
        # print(dp(0,0))
        # print(cache)
        return stringToValue(s1) + stringToValue(s2) - dp(0,0)*2

        