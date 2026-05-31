class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        out = list()
        c = 1
        for i in range(1, n+1):
            # print(i, c, target[c-1])
            # print(i, c, len(target))
            if c > len(target):
                break
            
            if i != target[c-1]:
                out.append("Push")
                out.append("Pop")
                continue
            
            out.append("Push")
            c+=1
            continue
            

        return out