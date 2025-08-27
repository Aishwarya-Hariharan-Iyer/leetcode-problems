class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)

        if l == 0:
            return -1

        if l == 1:
            return 0

        vals = dict({})
        for c in s:
            vals[c] = vals.get(c, 0) + 1
        
        for i in range(l):
            c = s[i]
            if vals[c] == 1:
                return i
        
        return -1
        
