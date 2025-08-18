class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = dict({})
        
        for c in s:
            count[c] = count.get(c, 0) + 1
        
        length = 0
        has_middle_char = False

        for c in count.keys():
            i = count[c]
            length += (i if i % 2 == 0 else i-1)
            has_middle_char = has_middle_char or (i % 2 == 1)
        
        return length + (0 if not has_middle_char else 1)

        
