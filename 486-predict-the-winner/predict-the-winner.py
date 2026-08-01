class Solution(object):
    def predictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n=len(nums)
        def help(i,j,p1,p2,turn):
            if(i>j):
                return p1>=p2
            if(turn):
                return (help(i+1,j,p1+nums[i],p2,False) or help(i,j-1,p1+nums[j],p2,False))
            else:
                    return (help(i+1,j,p1,p2+nums[i],True) and  help(i,j-1,p1,p2+nums[j],True))
        return help(0,n-1,0,0,True)  