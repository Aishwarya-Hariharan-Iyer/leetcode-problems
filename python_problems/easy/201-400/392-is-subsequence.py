class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        sptr = 0
        tptr = 0
        
        ls = len(s)
        lt = len(t)

        if ls == 0:
            return True

        if lt == 0:
            return ls == lt
        
        if ls > lt:
            return False
        
        while tptr < lt and sptr < ls:
            if s[sptr] == t[tptr]:
                tptr += 1
                sptr += 1
            else:
                tptr += 1
        
        return sptr == ls

