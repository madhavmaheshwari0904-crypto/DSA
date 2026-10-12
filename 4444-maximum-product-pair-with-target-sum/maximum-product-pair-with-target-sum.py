class Solution(object):
    def maxProductPair(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        m = float('-inf')
        ans = [-1, -1]
        map_ = {}
        for i, x in enumerate(nums):
            complement = target - x
            if complement in map_:
                j = map_[complement]
                p = nums[j] * x
                if x > complement:
                    if p > m:
                        m = p
                        ans = [i, j]
                elif complement > x:
                    if p > m:
                        m = p
                        ans = [j, i]
            map_[x] = i
        return ans