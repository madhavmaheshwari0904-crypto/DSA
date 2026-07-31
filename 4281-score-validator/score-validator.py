class Solution(object):
    def scoreValidator(self, events):
        """
        :type events: List[str]
        :rtype: List[int]
        """
        c=0
        s=0
        for i in events:
            if i=="W":
                c+=1
                if c>=10:
                    break
            else:
                if(len(i)==2):
                    s+=1
                else:
                    s+=int(i)
        return [s,c]