class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        ln = len(needle)
        lh = len(haystack)
        if ln > lh:
            return -1
        for i in range(lh-ln+1):
            if haystack[i:i+ln] == needle:
                return i
        return -1
        
