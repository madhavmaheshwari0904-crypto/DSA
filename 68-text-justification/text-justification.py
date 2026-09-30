class Solution(object):
    def fullJustify(self, words, maxwidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        ans=[]
        i=0
        while(i<len(words)):
            j=i+1
            s=0
            s=len(words[i])
            while(j<len(words) and s+1+len(words[j])<=maxwidth):
                s=s+1+len(words[j])
                j+=1
            line=""
            diff=j-i-1
            if j == len(words) or diff == 0:
                line += words[i]
                for k in range(i + 1, j):
                    line += " " + words[k]
                while len(line) < maxwidth:
                    line += " "
            else:
                total = sum(len(words[k]) for k in range(i, j))
                total_spaces = maxwidth - total
                spaces = total_spaces // diff
                extra_spaces = total_spaces % diff
                
                line += words[i]
                for k in range(i + 1, j):
                    spaces_to_add = spaces + (1 if extra_spaces > 0 else 0)
                    if extra_spaces > 0:
                        extra_spaces -= 1
                        
                    line += " " * spaces_to_add + words[k]
            ans.append(line)
            i=j
        return ans