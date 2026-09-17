class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s in {
            "nan", "inf", "+inf", "-inf",
            "Infinity", "+Infinity", "-Infinity"
        }:
            return False
        try:
            float(s)
            return True
        except ValueError:
            return False