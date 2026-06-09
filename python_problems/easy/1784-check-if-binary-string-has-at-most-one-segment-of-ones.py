class Solution(object):
    def checkOnesSegment(self, s):
        """
        :type s: str
        :rtype: bool
        """
        seg_start = False
        seg_over = False

        for c in s:
            if c == '1' and not seg_start and not seg_over:
                seg_start = True
            if c == '0' and seg_start:
                seg_over = True
                seg_start = False
            if c == '1' and not seg_start and seg_over:
                return False
        return True
        
