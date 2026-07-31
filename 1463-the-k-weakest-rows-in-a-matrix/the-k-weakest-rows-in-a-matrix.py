class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        fre={}
        for i in range(len(mat)):
            c=mat[i].count(1)
            fre[i]=c
        return sorted(fre,key=fre.get)[:k]

