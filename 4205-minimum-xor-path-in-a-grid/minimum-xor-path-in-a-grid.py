class Solution(object):
  def minCost(self, grid):
    """:type grid: List[List[int]]

    :rtype: int
    """
    n, m = len(grid), len(grid[0])
    dp = [[set() for _ in range(m)] for _ in range(n)]
    dp[0][0].add(grid[0][0])
    for i in range(n):
      for j in range(m):
        if i == 0 and j == 0:
          continue
        curr_val = grid[i][j]
        incoming = set()
        if i > 0:
          for x in dp[i - 1][j]:
            incoming.add(x ^ curr_val)
        if j > 0:
          for x in dp[i][j - 1]:
            incoming.add(x ^ curr_val)
        dp[i][j] = incoming
    return min(dp[n - 1][m - 1])