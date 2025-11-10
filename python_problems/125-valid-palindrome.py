import re

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip().lower()
        s = ''.join(re.findall('[a-z0-9]*', s))
        if not s:
            return True
        l = len(s)
        lp = 0
        rp = l-1
        if l == 0 or l == 1:
            return True
        while lp <= rp:
            if s[lp] != s[rp]:
                return False
            lp += 1
            rp -= 1
            
        return True
        
