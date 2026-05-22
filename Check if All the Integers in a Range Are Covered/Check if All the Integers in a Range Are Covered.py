class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        events = defaultdict(int)

        for l, r in ranges:
            events[l] += 1
            events[r+1] -= 1

        # print(events)
        sEvents = sorted(events.items())
        curr = 0

        for loc, change in sEvents:
            if loc > left:
                break
            curr += change
        # print(left, right)
        for i in range(left, right+1):
            print(i)
            curr += events[i]

            if curr < 0:
                return False

        return True