class WordFilter(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.d={}
        for w in range(len(words)):
            word=words[w]
            for j in range(len(word)-1,-1,-1):
                for i in range(len(word)):
                    curr_word=word[:i+1]+"#"+word[len(word)-j-1:]
                    self.d[curr_word]=w
        #print(self.d)

    def f(self, pref, suff):
        """
        :type pref: str
        :type suff: str
        :rtype: int
        """
        if pref+"#"+suff not in self.d:
            return -1
        return self.d[(pref+"#"+suff)]
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)