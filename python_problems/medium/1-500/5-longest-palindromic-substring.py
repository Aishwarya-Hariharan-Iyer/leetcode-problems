class Solution:
    def checkPalindrome(self, s):
        l = len(s)
        if l <= 1:
            return True
        lp = 0
        rp = l-1
        while lp <= rp:
            if s[rp] != s[lp]:
                return False
            lp += 1
            rp -= 1
        return True

    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        if l <= 1:
            return s

        for str_len in range(l, 1, -1):
            for i in range(0, l-str_len+1):
                if self.checkPalindrome(s[i:i+str_len]):
                    return s[i:i+str_len]
        
        return s[0]


class Solution:
    def checkPalindrome(self, s):
        l = len(s)
        if l <= 1:
            return True
        lp = 0
        rp = l-1
        while lp <= rp:
            if s[rp] != s[lp]:
                return False
            lp += 1
            rp -= 1
        return True

    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        if l <= 1:
            return s

        best_len = 1
        best_str = s[0]

        for i in range(l):
            for j in range(i, l):
                ss = s[i:j+1]
                ls = len(ss)
                if self.checkPalindrome(ss) and ls > best_len:
                    best_len = ls
                    best_str = ss
        
        return best_str

        