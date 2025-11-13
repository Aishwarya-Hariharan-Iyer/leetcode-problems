class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        if n == 0:
            return False

        while n > 1:
            if n % 2 == 1:
                return False
            n = n/2
        
        return n == 1

        
        
