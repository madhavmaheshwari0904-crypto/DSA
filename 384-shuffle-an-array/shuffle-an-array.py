class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.arr=nums[:]

    def reset(self):
        """
        :rtype: List[int]
        """
        return self.arr

    def shuffle(self):
        """
        :rtype: List[int]
        """
        ans=self.arr[:]
        """for i in range(len(ans)):
            swap=random.randrange(i,len(ans))
            ans[i],ans[swap]=ans[swap],ans[i]"""
        random.shuffle(ans)
        return ans    


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()