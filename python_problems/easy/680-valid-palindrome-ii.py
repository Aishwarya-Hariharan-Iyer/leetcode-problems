class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = len(s)
        if l <= 2:
            return True

        def check_normal_palindrome(s, lp, rp, free_pass_expired):
            while lp <= rp:
                if s[lp] != s[rp] and free_pass_expired:
                    return False
                elif s[lp] != s[rp]:
                    return check_normal_palindrome(s, lp+1, rp, True) or check_normal_palindrome(s, lp, rp-1, True)
                else:
                    lp += 1
                    rp -= 1
            return True

        return check_normal_palindrome(s, 0, l-1, False)
        
