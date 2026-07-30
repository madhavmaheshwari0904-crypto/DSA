class Solution(object):
    def countArrangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums=[i for i in range(1,n+1)]
        self.count=0
        def per(curr):
            if(curr==len(nums)):
                self.count+=1
                return
            for i in range(curr,len(nums)):
                if((nums[i]%(curr+1)==0)or((curr+1)%nums[i]==0)):
                    nums[i],nums[curr]=nums[curr],nums[i]
                    per(curr+1)
                    nums[i],nums[curr]=nums[curr],nums[i]
            return 
        per(0)
        return self.count                    