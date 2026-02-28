class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        indexes = dict()
        output = []

        for s in strs:
            curr = "".join(sorted(s))            
            # print(s, curr)
            if curr in indexes:
                output[indexes[curr]].append(s)
                continue
            
            indexes[curr] = len(output)
            output.append([s])

        return output