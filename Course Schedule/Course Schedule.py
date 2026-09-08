class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def recur(dfs, prerequisites) -> bool:
            # print(dfs)
            for i in range(len(prerequisites)):
                if prerequisites[i][1] != dfs[-1]:
                    continue
                # print(prerequisites[i][0])
                if prerequisites[i][0] in dfs:
                    return False
                
                dfs.append(prerequisites[i][0])
                if not recur(dfs, prerequisites):
                    return False
                dfs.pop(-1)
            return True

        for i in range(len(prerequisites)):
            dfs = [prerequisites[i][1]]
            if not recur(dfs, prerequisites):
                return False

        return True