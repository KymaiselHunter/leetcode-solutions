class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        product = 1

        for row in grid:
            for item in row:
                product *= item
        # print(product)

        out = [[(product // item) % 12345 for item in row]for row in grid]

        return out
