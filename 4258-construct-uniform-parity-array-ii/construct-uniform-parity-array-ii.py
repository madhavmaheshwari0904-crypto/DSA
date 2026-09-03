class Solution(object):
    def uniformArray(self, nums1):
        """
        :type nums1: List[int]
        :rtype: bool
        """
        mini=min(nums1)
        if(mini%2==1):
            return True
        else:
            for i in nums1:
                if(i%2==1):
                    return False
            return True