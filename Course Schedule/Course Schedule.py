class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mp = [[] for i in range(numCourses)]

        for i in range(len(prerequisites)):
            mp[prerequisites[i][0]].append(prerequisites[i][1])

        def recur(dfs, prerequisites) -> bool:
            for num in mp[dfs[-1]]:
                if num in dfs:
                    return False
                
                dfs.append(num)
                if not recur(dfs, prerequisites):
                    return False
                dfs.pop(-1)
            return True

        for i in range(numCourses):
            dfs = [i]
            if not recur(dfs, prerequisites):
                return False

        return True