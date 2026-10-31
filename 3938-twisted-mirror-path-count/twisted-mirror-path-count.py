class Solution(object):
    def uniquePaths(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        MOD = 10**9 + 7
        m = len(grid)
        n = len(grid[0])
        memo = {}
        def solve(r, c, direction):
            if r == m - 1 and c == n - 1:
                return 1
            if r < 0 or r >= m or c < 0 or c >= n:
                return 0
            state = (r, c, direction)
            if state in memo:
                return memo[state]
            total = 0
            if grid[r][c] == 1:
                if direction == 1:  
                    total = solve(r + 1, c, 0)
                else:            
                    total = solve(r, c + 1, 1)
            else:
                down = solve(r + 1, c, 0)
                right = solve(r, c + 1, 1)
                total = (down + right) % MOD
                
            memo[state] = total % MOD
            return memo[state]
        res_down = solve(1, 0, 0) if m > 1 else 0
        res_right = solve(0, 1, 1) if n > 1 else 0
        if m == 1 and n == 1:
            return 1
            
        return (res_down + res_right) % MOD