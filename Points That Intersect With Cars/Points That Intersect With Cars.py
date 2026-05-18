class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        d = defaultdict(int)

        for num in nums:
            start, end = num[0], num[1]+1

            d[start] += 1
            d[end] -= 1

        d = sorted(d.items())
        # print(d)
        active = 0
        answer = 0

        for index, (loc, val) in enumerate(d[:-1]):
            active += val

            start = loc
            end = d[index+1][0]-1

            length = end - start + 1

            if active > 0:
                answer += length

            print(index, val)
        return answer