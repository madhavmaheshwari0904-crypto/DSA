class Solution(object):
    def shortestCompletingWord(self, l, word):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        temp=[i.lower() for i in l if i.isalpha()]
        print(temp)
        word.sort(key=len)
        for i in word:
            f=True
            for j in temp:
                if(j not in i) or (i.count(j)<temp.count(j)):
                    f=False
                    break
            if f:
                return i    
