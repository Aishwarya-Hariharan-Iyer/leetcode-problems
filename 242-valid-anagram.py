class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ls = len(s)
        lt = len(t)
        if ls != lt:
            return False

        s_count = dict({})
        t_count = dict({})
        for c in s:
            s_count[c] = s_count.get(c, 0) + 1
        
        for c in t:
            t_count[c] = t_count.get(c, 0) + 1

        for c in s_count.keys():
            if s_count[c] != t_count.get(c, 0):
                return False
        return True
