class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        def solve(goal):
            if goal < 0:
                return 0

            i = 0
            c = 0
            s = 0

            for j in range(len(nums)):
                s += nums[j]
                while s > goal:
                    s -= nums[i]
                    i += 1
                c += j - i + 1
            return c
        return solve(goal)-solve(goal-1)                