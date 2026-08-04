class Solution(object):
    def countDistinctIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num=set()
        for i in nums:
            num.add(i)
            num.add(int(str(i)[::-1]))
        return len(num)            
