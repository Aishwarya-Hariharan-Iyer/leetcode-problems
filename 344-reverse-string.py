class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        l = len(s)
        temp = ""
        if l == 1:
            return s
        for i in range(l/2):
            temp = s[l-1-i]
            s[l-1-i] = s[i]
            s[i] = temp
        return s
    
