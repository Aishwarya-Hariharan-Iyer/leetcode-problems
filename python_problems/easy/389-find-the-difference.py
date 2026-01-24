class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        hashmap = dict()
        
        for c in s:
            hashmap[c] = hashmap.get(c, 0) + 1
        
        for c in t:
            if hashmap.get(c, 0) == 0:
                return c
            else:
                hashmap[c] = hashmap.get(c) - 1

        return ""
        