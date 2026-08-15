class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        l=0
        h=len(arr)-1
        while(l<=h):
            mid=l+(h-l)//2
            miss=arr[mid]-(mid+1)
            if(miss<k):
                l=mid+1
            else:
                h=mid-1
        return h+k+1        