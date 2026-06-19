class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        def isGoodString(x):
            return x[0] != x[1] and x[1] != x[2] and x[0] != x[2]

        l = len(s)

        count = 0

        for i in range(l-2):
            if isGoodString(s[i:i+4]):
                count += 1

        return count 
        
