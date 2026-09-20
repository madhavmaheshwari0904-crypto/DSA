from sortedcontainers import SortedList
class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        ans=[]
        window=SortedList()
        for i in range(k):
            window.add(nums[i])
        def get_median():
            if k % 2 == 1:
                return float(window[k // 2])
            else:
                return (window[k // 2 - 1] + window[k // 2]) / 2.0
        ans.append(get_median())
        for i in range(k,len(nums)):
            window.add(nums[i])
            window.remove(nums[i-k])
            ans.append(get_median())
        return ans