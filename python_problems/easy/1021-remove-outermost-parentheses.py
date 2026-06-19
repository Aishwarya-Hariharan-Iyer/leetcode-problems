class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ls = len(s)
        if ls == 0:
            return s
        lptr = 0
        count = 0
        s = list(s)
        while lptr < ls:
            if s[lptr] == "(":
                count += 1
                if count == 1: #outermost
                    s[lptr] = ""
                lptr += 1
            else: # ")"
                count -= 1
                if count == 0: #outermost
                    s[lptr] = ""
                lptr += 1
        return "".join(s)

        
