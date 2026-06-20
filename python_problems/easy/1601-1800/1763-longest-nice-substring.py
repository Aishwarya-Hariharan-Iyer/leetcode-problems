class Solution:

    def longestNiceSubstring(self, s: str) -> str:
        
        l = len(s)
        if l < 2:
            return ""

        chars = set(s)

        bad_index = -1
        for i in range(l):
            if s[i].swapcase() not in chars:
                bad_index = i
                break
        
        if bad_index == -1:
            return s

        else:
            s1 = self.longestNiceSubstring(s[:bad_index])
            s2 = self.longestNiceSubstring(s[bad_index+1:])
            return s1 if len(s1) >= len(s2) else s2