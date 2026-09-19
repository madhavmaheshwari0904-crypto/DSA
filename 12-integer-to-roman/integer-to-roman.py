class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        num_map = [
            (1000, "M"), (900, "CM"),
            (500, "D"),  (400,"CD"),
            (100, "C"),  (90,"XC"),
            (50, "L"),   (40,"XL"),
            (10,"X"),   (9,"IX"),
            (5,"V"),    (4,"IV"),
            (1 ,"I")]
        ans=[]
        """for i in [1000,900,500,400,100,90,50,40,10,9,5,4,1]:
            while(i<=num):
                ans=ans+num_map[i]
                num-=i
        return ans  """
        for val,sym in num_map:
            if(val==0):
                break
            c=num/val
            num=num%val
            ans.append(c*sym)
            print(c)
            print(num)
        return ''.join(ans)
        