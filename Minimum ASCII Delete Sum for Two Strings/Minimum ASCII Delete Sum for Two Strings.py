class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        def stringToValue(s: str):
            output = 0
            for letter in s:
                output += ord(letter)

            return output

        map1 = dict()
        map2 = dict()

        def recur(s: str, map: dict) -> None:
            if s in map:
                # print(map)
                return
            # print("no return")
            map[s] = stringToValue(s)
            
            for i in range(len(s)):
                # print(s[0:i] + s[i+1::])
                recur(s[0:i] + s[i+1::], map)

        # map1[s1] = stringToValue(s1) 
        recur(s1, map1)
        recur(s2, map2)
        # print(set(map1.values()))
        # print(set(map2.values())) 
        keys = map1.keys() & map2.keys()
        # print(keys)
        # value1 = stringToValue(s1)
        # value2 = stringToValue(s2) 
        inputValue = stringToValue(s1) + stringToValue(s2)
        outputs = [inputValue - map1[key]*2 for key in keys]
        # print(outputs)        
        return min(outputs)