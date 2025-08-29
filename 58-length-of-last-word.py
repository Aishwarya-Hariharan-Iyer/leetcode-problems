class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.strip().split(" ")
        return len(words[-1]) if len(words) >= 1 else 0

        
