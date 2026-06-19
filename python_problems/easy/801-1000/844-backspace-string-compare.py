class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ls = len(s)
        lt = len(t)
        l = ls if ls > lt else lt
        sa = []
        ta = []
        
        for i in range(l):
            if i < ls and s[i] == "#":
                sa = sa[:-1]
            if i < ls and s[i] != "#":
                sa.append(s[i])
            if i < lt and t[i] == "#":
                ta = ta[:-1]
            if i < lt and t[i] != "#":
                ta.append(t[i])

        return ''.join(sa) == ''.join(ta)
