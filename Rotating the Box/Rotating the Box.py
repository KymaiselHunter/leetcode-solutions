class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        out = [['.' for i in range(len(boxGrid))] for j in range(len(boxGrid[0]))]

        for i in range(len(boxGrid)):
            q = list()
            for j in range(len(boxGrid[i])):
                curr = boxGrid[i][j]
                if curr == '.':
                    continue
                if curr == '*':
                    q.append((i, j))
                    continue

                q.append('#')

            col = len(boxGrid)-i-1
            row = len(out) - 1

            while q:
                curr = q.pop(-1)
                if curr is '#':
                    out[row][col] = '#'
                    row -= 1
                    continue
                # print(curr, row)
                row = curr[1]
                out[row][col] = '*'
                row -= 1

        return out