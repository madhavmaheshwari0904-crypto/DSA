class Solution(object):
    def findLongestWord(self, s, dictionary):
        """
        :type s: str
        :type dictionary: List[str]
        :rtype: str
        """
        dictionary.sort(key=lambda x:(-len(x),x))
        #print( dictionary)
        for word in  dictionary:
            i=0
            for j in s:
                if(i<len(word) and j==word[i]):
                    i+=1
                    if(i==len(word)):
                        break
            if i==len(word):
                return word
        return ''                