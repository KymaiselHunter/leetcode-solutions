class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        out = float('inf')
        ear1 = out
        ear2 = out

        for i in range(len(landStartTime)):
            ear1 = min(ear1, landStartTime[i] + landDuration[i])

        for i in range(len(waterStartTime)):
            ear2 = min(ear2, waterStartTime[i] + waterDuration[i])

            if ear1 <= waterStartTime[i]:
                out = min(out, waterStartTime[i] + waterDuration[i])
            else:
                out = min(out, ear1 + waterDuration[i])
        
        for i in range(len(landStartTime)):
            if ear1 <= landStartTime[i]:
                out = min(out, landStartTime[i] + landDuration[i])
            else:
                out = min(out, ear2 + landDuration[i])
        return out