class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x == 1 or x == 0:
            return x

        l = 1
        u = x
        m = (u-l+1)/2
    
        while l <= u:
            m = (u+l)/2
            if m * m == x or ( m * m < x and (m+1) * (m+1) > x):
                return m
            if m * m < x:
                l = m + 1
            elif m * m > x:
                u = m - 1
        


        
        
