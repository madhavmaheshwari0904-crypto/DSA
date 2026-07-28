class Solution(object):
    def isValid(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if(len(word)<3):
            return False
        v=0
        c=0
        vowel_set = "aeiouAEIOU"
        for i in word:
            if i.isalpha():
                if(i in vowel_set):
                    v+=1
                else:
                    c+=1
            elif not i.isdigit():
                return False
        return v>=1 and c>=1                    