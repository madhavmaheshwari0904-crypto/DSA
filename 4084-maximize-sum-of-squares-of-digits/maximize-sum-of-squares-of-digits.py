class Solution(object):
    def maxSumOfSquares(self, num, sum):
        """
        :type num: int
        :type sum: int
        :rtype: str
        """
        if num*9<sum:
            return ""
        else:
            q=sum//9
            rem=sum%9
            ans=("9" * q) + (str(rem) if rem else "")
            return ans+"0"*(num-len(ans))
        
        