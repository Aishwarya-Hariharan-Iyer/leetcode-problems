class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        xs = str(x)
        l = len(xs)
        lp = 0
        rp = l - 1
        while lp <= rp:
            if xs[lp] != xs[rp]:
                return False
            lp += 1
            rp -= 1
        return True

        
