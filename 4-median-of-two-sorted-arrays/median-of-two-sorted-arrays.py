class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n1, n2 = len(nums1), len(nums2)
        total_len = n1 + n2
        i1 = total_len // 2 - 1
        i2 = total_len // 2
        e1, e2 = -1, -1
        p1, p2, i = 0, 0, 0
        while(p1<n1 and p2<n2):
            if(nums1[p1]<=nums2[p2]):
                if(i==i1):
                    e1=nums1[p1]
                if(i==i2):
                    e2=nums1[p1]
                p1+=1
                i+=1
            else:
                if(i==i1):
                    e1=nums2[p2]
                if(i==i2):
                    e2=nums2[p2]
                p2+=1
                i+=1
        while(p1<n1):
            if(i==i1):
                e1=nums1[p1]
            if(i==i2):
                e2=nums1[p1]
            i+=1
            p1+=1
        while(p2<n2):
            if(i==i1):
                e1=nums2[p2]
            if(i==i2):
                e2=nums2[p2]
            i+=1
            p2+=1
        #print(e1)
        #print(e2)
        if(total_len%2==0):
            return (e1+e2)/2.0
        else:
            return e2