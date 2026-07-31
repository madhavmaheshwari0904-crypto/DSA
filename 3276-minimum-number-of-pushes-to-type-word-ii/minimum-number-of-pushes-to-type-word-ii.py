class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        fre=Counter(word)
        l=sorted(fre.values(),reverse=True)
        print(l)
        ans=0
        for i,j in enumerate(l):
            f=(i//8)+1
            ans+=f*j
        return ans    