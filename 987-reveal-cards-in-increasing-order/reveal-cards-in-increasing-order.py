class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        deck.sort()
        m=[]
        for i in range(0,len(deck)):
            m.append(i)
        ans=[0]*len(deck)
        for i in range(len(deck)):
            ans[m.pop(0)]=deck[i]
            if m:
                m.append(m.pop(0))
        return ans    
