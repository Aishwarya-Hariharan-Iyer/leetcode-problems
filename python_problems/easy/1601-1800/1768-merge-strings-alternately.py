class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merged = ""
        ltr = 0
        rtr = 0
        l1 = len(word1)
        l2 = len(word2)

        while ltr < l1 or rtr < l2:
            if ltr == l1:
                return merged + word2[rtr:]
            elif rtr == l2:
                return merged + word1[ltr:]
            else:
                merged += word1[ltr] + word2[rtr]
                ltr += 1
                rtr += 1
        
        return merged
        
