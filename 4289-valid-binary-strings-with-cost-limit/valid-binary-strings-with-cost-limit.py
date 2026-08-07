class Solution(object):
    def generateValidStrings(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[str]
        """
        l=[]
        def back(n,s="",c=0):
            if(len(s)==n):
                l.append(s)
                return None
            if not c:
                back(n,s+"1",1)
            back(n,s+"0",0)
        back(n)  

        ans=[]
        for i in l:
            c=0
            for j in range(len(i)):
                if(i[j]=="1"):
                    c+=j
            if c<=k:
                ans.append(i)
        return ans                 