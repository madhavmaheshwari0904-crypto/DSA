class Solution(object):
    def sumCounts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        ans=[]
        for i in range(n):
            l=set()
            c=0
            for j in range(i,n):
                if nums[j] not in l:
                    l.add(nums[j])
                    c+=1
                    ans.append(c)
                else:
                    ans.append(c)
        print(ans)
        return sum(i*i for i in ans)