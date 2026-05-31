class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        heapq.heapify(asteroids)

        while asteroids:
            curr = heapq.heappop(asteroids)
            if curr > mass:
                return False
            mass += curr
        return True 