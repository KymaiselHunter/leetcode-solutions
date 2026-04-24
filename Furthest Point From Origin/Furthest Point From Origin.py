class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        greedyLeft = 0
        greedyRight = 0

        for char in moves:
            if char == '_':
                greedyLeft += 1
                greedyRight += 1
            else:
                if char == 'L':
                    greedyLeft += 1
                    greedyRight -= 1
                else:
                    greedyRight += 1
                    greedyLeft -= 1
                
        return max(greedyLeft, greedyRight)