# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        li = 1
        ui = n
        
        while (li <= ui):
            if isBadVersion(li):
                return li
            else:
                mi = (ui+li)/2
                if isBadVersion(mi):
                    ui = mi
                else:
                    li = mi+1
