class Solution(object):
    def digitSum(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if(len(s)<=k):
            return s
        m=""
        for i in range(0,len(s),k):
            g=s[i:i+k]
            n=sum(int(j) for j in str(g))
            m+=str(n)
        return self.digitSum(m,k)          
        