class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mp = [[] for i in range(numCourses)]

        for i in range(len(prerequisites)):
            mp[prerequisites[i][0]].append(prerequisites[i][1])

        cache = set()

        def recur(prev, dfs) -> bool:
            for num in mp[prev]:
                if prev in cache:
                    return True
                
                if num in dfs:
                    return False
                
                dfs.add(num)
                if not recur(num, dfs):
                    return False
                dfs.remove(num)
                cache.add(num)
            return True

        for i in range(numCourses):
            dfs = set()
            dfs.add(i)
            if not recur(i, dfs):
                return False

        return True