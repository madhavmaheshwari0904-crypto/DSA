class Solution(object):
    def numOfWays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mod = 10**9 + 7
        n = len(nums)
        comb = [[0] * n for _ in range(n)]
        for i in range(n):
            comb[i][0] = 1
            for j in range(1, i + 1):
                comb[i][j] = (comb[i - 1][j - 1] + comb[i - 1][j]) % mod
                
        def solve(sub_nums):
            if len(sub_nums) <= 2:
                return 1
            
            root = sub_nums[0]
            left = []
            right = []
            
            for y in sub_nums[1:]:
                if y < root:
                    left.append(y)
                else:
                    right.append(y)
            
            left_ways = solve(left)
            right_ways = solve(right)
            m = len(left)
            k = len(right)
            return comb[m + k][m] * left_ways % mod * right_ways % mod
            
        return (solve(nums) - 1) % mod