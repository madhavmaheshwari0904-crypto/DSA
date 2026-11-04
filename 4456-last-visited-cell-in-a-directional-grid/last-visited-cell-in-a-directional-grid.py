class Solution(object):
    def lastVisitedCell(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: List[int]
        """
        n, m = len(grid), len(grid[0])
        i, j = 0, 0
        while True:
            c = grid[i][j]
            a, b = i, j
            if c == 'L':
                b -= 1
            elif c == 'R':
                b += 1
            elif c == 'U':
                a -= 1
            else:
                a += 1
            if a < 0 or a >= n or b < 0 or b >= m or grid[a][b] == '0':
                return [i, j]
            grid[i][j] = '0'
            i, j = a, b
        return [i, j]