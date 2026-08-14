class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if arr.count(0) >= 2:
            return True
        for i in range(len(arr)):
            if(arr[i]*2 in arr and arr[i]!=0):
                return True
        return False        